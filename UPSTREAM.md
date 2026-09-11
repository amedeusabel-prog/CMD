# Provenance

Verified 2026-09-11 by byte-for-byte `diff` of every file that was in `amedeusabel-prog/CMD` at commit `9abba970` ("Add files via upload") against fresh clones of the two upstream repositories.

## Pinned sources

| Vendored tree | Upstream | Ref | Commit | License |
|---|---|---|---|---|
| `upstream/hyperresearch/` | github.com/jordan-gibbs/hyperresearch | `v0.9.1` | `183443aefec8d0444f4b53095cee17bf77ad5fb2` | MIT, © 2026 Jordan Gibbs |
| `upstream/no-ai-slop/` | github.com/petergyang/no-ai-slop | `main` | `000650b156983f5159695b441477f4e63b25dc85` (plugin `1.0.6`) | MIT, © 2026 Peter Yang |

Vendored with `.git/` removed; 210 files, 2.6 MB; no file in `upstream/` was edited.

## 45 files deleted as duplicates

Each was byte-identical to the upstream path shown. `upstream/` now carries the real one.

| Deleted from repo root | Identical to |
|---|---|
| `base.py`, `builtin.py`, `crawl4ai_provider.py`, `exa_provider.py`, `tavily_provider.py`, `__init__.py` | `upstream/hyperresearch/src/hyperresearch/web/` |
| `graph.py`, `note.py`, `output.py`, `search.py` | `upstream/hyperresearch/src/hyperresearch/models/` |
| `__main__.py`, `py.typed` | `upstream/hyperresearch/src/hyperresearch/` |
| `ci.yml`, `publish.yml` | `upstream/hyperresearch/.github/workflows/` (inert at repo root — Actions only reads `.github/workflows/`) |
| `hyperresearch.md`, `hyperresearch-1…16*.md` (19 files) | `upstream/hyperresearch/src/hyperresearch/skills/` |
| `phase-0…5*.md`, `README.md` | `upstream/hyperresearch/docs/roadmap-2.0/` |
| `hyperresearch-0.9.1-LICENSE`, `hyperresearch-0.9.1.gitignore` | `upstream/hyperresearch/LICENSE`, `.gitignore` (renamed copies) |
| `LICENSE`, `PRIVACY.md`, `TERMS.md`, `no-ai-slop.png` | `upstream/no-ai-slop/` (`LICENSE`, `PRIVACY.md`, `TERMS.md`, `assets/`) |

`README.md` was a copy of the upstream roadmap README; it has been replaced by the repository index.

## 3 files that are not upstream — `local-modifications/no-ai-slop/`

These are the only files in the old repo that differ from any release. They are copies of `no-ai-slop` v1.0.6 files, edited, and re-versioned in `plugin.json` to `1.1.0` — a version that does not exist upstream.

| File | Delta vs upstream v1.0.6 |
|---|---|
| `SKILL.md` | 72 changed lines. Adds a `## Statistical fingerprints to fix` section (perplexity, burstiness, cohesion, vocabulary clustering, paragraph symmetry, meta-signposting), tuned to "the deeper patterns **AI detectors** notice", plus matching edits to the principles list |
| `eval.md` | 51 changed lines. Adds the checklist block that scores a rewrite against those fingerprints |
| `plugin.json` | 10 changed lines. Re-describes the plugin around detector evasion; still credits `author: Peter Yang` |

Reference check: `grep -ciE "perplexity|burstiness|fingerprint|detector" upstream/no-ai-slop/skills/no-ai-slop/SKILL.md` → **0**. The section has no upstream origin.

Two problems with these files as they stand:

1. **Attribution.** `plugin.json` keeps `author.name = "Peter Yang"` and `repository = github.com/petergyang/no-ai-slop` while describing changes he did not make, at a fake version number. MIT permits derivation, not implied endorsement — a derivative needs its own authorship and a name that does not impersonate `1.1.0`.
2. **Purpose drift.** The upstream skill edits drafts toward clarity and explicitly refuses detector work: `SKILL.md` (upstream) reads *"AI detectors guess. Named patterns are evidence the user can check."* The local section reorients the same text toward what detectors key on. That is the difference between a copy-editing aid and an authorship-misrepresentation aid, and it is why these three files are parked rather than integrated.
