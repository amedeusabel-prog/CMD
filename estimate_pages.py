# -*- coding: utf-8 -*-
"""
Page-layout simulator for the proposal DOCX.

Wraps every paragraph with real Times-Roman/Times New Roman glyph advance
widths at the exact text width produced by the guide's margins, applies the
guide's line spacing (double for text, single for headings/tables), and counts
pages. Used to keep the proposal inside the guide's 15-20 page rule.
"""
import math
import sys

# Times-Roman advance widths, 1/1000 em (Adobe AFM). Times New Roman is
# metrically very close to Times-Roman.
W = {
    ' ': 250, '!': 333, '"': 408, '#': 500, '$': 500, '%': 833, '&': 778, "'": 180,
    '(': 333, ')': 333, '*': 500, '+': 564, ',': 250, '-': 333, '.': 250, '/': 278,
    ':': 278, ';': 278, '<': 564, '=': 564, '>': 564, '?': 444, '@': 921,
    '[': 333, '\\': 278, ']': 333, '^': 469, '_': 500, '`': 333,
    '{': 480, '|': 200, '}': 480, '~': 541, '\u2193': 500, '\u03b2': 500,
    '\u2080': 300, '\u2081': 300, '\u2082': 300, '\u2083': 300, '\u03b5': 444,
    '\u00b2': 300, '\u00d7': 564, '\u2019': 333, '\u2013': 500, '\u2014': 667,
}
for c, w in zip('0123456789', [500] * 10):
    W[c] = w
for c, w in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                [722, 667, 667, 722, 611, 556, 722, 722, 333, 389, 722, 611, 889, 722,
                 722, 556, 722, 667, 556, 611, 722, 722, 944, 722, 722, 611]):
    W[c] = w
for c, w in zip('abcdefghijklmnopqrstuvwxyz',
                [444, 500, 444, 500, 444, 333, 500, 500, 278, 278, 500, 278, 778, 500,
                 500, 500, 500, 333, 389, 278, 500, 500, 722, 500, 500, 444]):
    W[c] = w

PAGE_H = (29.7 - 2.54 - 2.54) * 28.3465   # 697.6 pt usable text height (top margin 1 inch)
PAGE_W = (21.0 - 4.0 - 2.54) * 28.3465     # 409.9 pt usable text width
SINGLE = {12: 13.79, 14: 16.09}            # line height = 1.149 em
DOUBLE = {k: v * 2 for k, v in SINGLE.items()}
CELL_MARGIN_PT = 2 * (0.19 * 28.3465)      # left+right cell margins


def text_width(s, size, bold=False):
    w = sum(W.get(ch, 500 if ch.isupper() else 450) for ch in s)
    return w / 1000.0 * size * (1.035 if bold else 1.0)


def wrap_lines(text, size, width, bold=False):
    """Greedy word wrap; returns number of lines."""
    text = text.replace('*', '')
    words = text.split(' ')
    lines, cur = 1, ''
    for word in words:
        trial = word if not cur else cur + ' ' + word
        if text_width(trial, size, bold) <= width:
            cur = trial
        else:
            if cur:
                lines += 1
            cur = word
            while text_width(cur, size, bold) > width and len(cur) > 1:
                # very long token: force-break
                cut = len(cur)
                while cut > 1 and text_width(cur[:cut], size, bold) > width:
                    cut -= 1
                cur = cur[cut:]
                lines += 1
    return lines


def simulate(blocks, refs_count=None, verbose=True):
    y = 0.0
    page = 1
    per = {}
    section = "Title page"

    def advance(h, tag, split=True, unit=None):
        nonlocal y, page
        if y + h <= PAGE_H:
            y += h
        elif split and unit:
            # flow block splits at line/row granularity across the page break
            room = max(0, int((PAGE_H - y) // unit))
            rest_lines = int(round(h / unit)) - room
            page += 1
            y = rest_lines * unit
            if y > PAGE_H:
                page += int(y // PAGE_H)
                y = y % PAGE_H
        else:
            page += 1
            y = h
        per[tag] = per.get(tag, 0.0) + h

    for kind, payload in blocks:
        if kind == 'h1':
            section = payload
            lines = wrap_lines(payload.upper(), 14, PAGE_W, bold=True)
            advance(4 + lines * SINGLE[14] + 2, section, split=False)
        elif kind == 'h2':
            lines = wrap_lines(payload, 14, PAGE_W, bold=True)
            advance(6 + lines * SINGLE[14] + 0, section, split=False)
        elif kind == 'h3':
            lines = wrap_lines(payload, 12, PAGE_W, bold=True)
            advance(4 + lines * SINGLE[12] + 0, section, split=False)
        elif kind == 'p' or kind == 'ref':
            lines = wrap_lines(payload, 12, PAGE_W)
            unit = DOUBLE[12]
            h = lines * unit
            if y + h <= PAGE_H:
                advance(h, section, split=False)
            else:
                # Word widow/orphan control: never leave a single line alone on
                # either side of a page break.
                room = int((PAGE_H - y) // unit)
                if room >= 2 and (lines - room) >= 2:
                    advance(room * unit, section, split=False)
                    page += 1
                    y = (lines - room) * unit
                    per[section] = per.get(section, 0.0) + (lines - room) * unit
                elif room >= 2 and (lines - room) == 1:
                    advance((room - 1) * unit, section, split=False)
                    page += 1
                    y = (lines - room + 1) * unit
                    per[section] = per.get(section, 0.0) + (lines - room + 1) * unit
                else:
                    advance(h, section, split=False)
        elif kind == 'caption':
            lines = wrap_lines(payload, 12, PAGE_W, bold=True)
            advance(4 + lines * SINGLE[12] + 2, section, split=False)
        elif kind == 'source':
            lines = wrap_lines(payload, 12, PAGE_W)
            advance(2 + lines * SINGLE[12] + 4, section, split=False)
        elif kind == 'table':
            rows = payload['rows']
            widths = payload.get('widths') or []
            merge = payload.get('merge', False)
            total = 0.0
            for ri, row in enumerate(rows):
                cell_lines = []
                for ci, cell in enumerate(row):
                    if merge and ri in (0, 2, 3, 4, 5):
                        w_cm = sum(widths) if widths else 14.46
                    else:
                        w_cm = widths[ci] if ci < len(widths) else 4.0
                    wpt = w_cm * 28.3465 - CELL_MARGIN_PT
                    n = 0
                    for ln in cell.split('\n'):
                        n += wrap_lines(ln, 12, wpt, bold=(ri == 0 and payload.get('header', True)))
                    cell_lines.append(max(1, n))
                total += max(cell_lines) * SINGLE[12] + 3
            advance(total, section, split=True, unit=SINGLE[12] + 3)
        elif kind == 'pagebreak':
            continue
    if verbose:
        print("Section pages (body only, usable height %.0f pt/page):" % PAGE_H)
        for k, v in per.items():
            print("   %-50s %6.0f pt  %5.2f pages" % (k[:50], v, v / PAGE_H))
        print("   %-50s %6.0f pt  %5.2f pages (packed)" % ("TOTAL BODY", sum(per.values()),
                                                  sum(per.values()) / PAGE_H))
        print("   Simulated page count (body): %d" % page)
        print("   + 1 title page  =>  ESTIMATED TOTAL: %d pages" % (page + 1))
    return page + 1, per
