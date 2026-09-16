# -*- coding: utf-8 -*-
"""Generates proposal_content.py from the compressed section text (NEW) plus the
tables, captions and reference list defined below."""
import ast
import pprint

NEW = ast.literal_eval(open('proposal_content.py.new', encoding='utf-8').read())

# Sections whose text is unchanged from the working draft
KEEP = {
 '1.4 Objectives of the Study': {
   'h3': [('1.4.1 General Objective',
           ["To assess the impact of the monitoring and evaluation system on the performance of "
            "local government projects in Lushoto District, Tanga Region."]),
          ('1.4.2 Specific Objectives',
           ["(i) To examine the extent to which M&E planning practices influence the performance "
            "of local government projects in Lushoto District; (ii) to assess the influence of "
            "M&E human resource capacity on the performance of local government projects in "
            "Lushoto District; and (iii) to determine the influence of stakeholder involvement in "
            "M&E on the performance of local government projects in Lushoto District."])]},
 '4.0 RESEARCH BUDGET': {
   'paras': ["The tentative budget below covers the items and services required to implement the "
             "study. Funds will come from the researcher's personal savings, with supplementary "
             "support from the Institute where available."]},
 '5.0 RESEARCH ACTION PLAN': {
   'paras': ["The activities below will be undertaken in the sequence and periods indicated, "
             "allowing for proposal defence, permits, pilot testing, fieldwork, analysis, report "
             "writing and submission."]},
}

FIGURE1 = ([["INDEPENDENT VARIABLES", "", ""],
            ["M&E planning practices\n- M&E plans\n- baselines, indicators, targets\n"
             "- budget, tools, schedules",
             "M&E human resource capacity\n- number of M&E staff\n- qualifications and training\n"
             "- experience and analysis skills",
             "Stakeholder involvement in M&E\n- beneficiaries and community\n"
             "- ward and village committees\n- contractors, PO-RALG, partners"],
            ["\u2193", "", ""],
            ["INTERVENING VARIABLES: timely release of funds; political will; legal and "
             "institutional framework; project complexity; M&E information systems", "", ""],
            ["\u2193", "", ""],
            ["DEPENDENT VARIABLE - Performance of local government projects: completion within "
             "schedule and budget; technical quality; utilisation and sustainability; "
             "beneficiary satisfaction", "", ""]],
           [4.9, 4.7, 4.8], False, True)

TABLE1 = ([["S/No", "Category of respondents", "N", "n"],
           ["1", "Council management team and heads of departments", "26", "7"],
           ["2", "Planning and M&E unit staff and sector M&E focal persons", "34", "9"],
           ["3", "Technical staff of implementing departments", "145", "39"],
           ["4", "Ward Executive Officers and ward councillors", "56", "16"],
           ["5", "Ward development committee members", "168", "45"],
           ["6", "Village Executive Officers and village chairpersons", "210", "56"],
           ["7", "Project and facility committee members", "385", "104"],
           ["8", "Contractors' and consultants' site personnel", "63", "17"],
           ["", "Total", "1,087", "293"]],
          [1.1, 9.1, 2.1, 2.1], True, False)

TABLE2 = ([["S/No", "Item / service", "Quantity", "Unit cost (TZS)", "Total (TZS)"],
           ["1", "Stationery, printing and photocopying", "Lump sum", "-", "450,000"],
           ["2", "Questionnaire administration (2 assistants, 14 days)", "28 days", "40,000", "1,120,000"],
           ["3", "Field transport within the district", "14 days", "65,000", "910,000"],
           ["4", "Travel to and from the study area", "4 trips", "120,000", "480,000"],
           ["5", "Subsistence and accommodation", "28 days", "70,000", "1,960,000"],
           ["6", "Pilot study", "30", "10,000", "300,000"],
           ["7", "Data analysis, statistical consultation and communication", "Lump sum", "-", "750,000"],
           ["8", "Printing, binding and defence logistics", "Lump sum", "-", "600,000"],
           ["", "Sub-total", "", "", "6,570,000"],
           ["", "Contingency at 10%", "", "", "657,000"],
           ["", "Grand total", "", "", "7,227,000"]],
          [1.1, 6.3, 2.4, 2.4, 2.6], True, False)

TABLE3 = ([["S/No", "Activity", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr"],
           ["1", "Proposal writing and submission", "X", "", "", "", "", "", "", ""],
           ["2", "Proposal defence and corrections", "", "X", "", "", "", "", "", ""],
           ["3", "Clearance, permits and entry meetings", "", "X", "X", "", "", "", "", ""],
           ["4", "Instrument development and pilot test", "", "", "X", "", "", "", "", ""],
           ["5", "Data collection in the field", "", "", "", "X", "X", "", "", ""],
           ["6", "Data cleaning, coding and analysis", "", "", "", "", "X", "X", "", ""],
           ["7", "Interpretation and report writing", "", "", "", "", "", "X", "X", ""],
           ["8", "Draft submission, binding and final defence", "", "", "", "", "", "", "X", "X"]],
          [1.0, 6.6, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95], True, False)

REFERENCES = [
 "Ba, A. (2021). How to measure monitoring and evaluation system effectiveness? *African "
 "Evaluation Journal, 9*(1), a553. https://doi.org/10.4102/aej.v9i1.553",
 "Creswell, J. W. (2014). *Research design: Qualitative, quantitative, and mixed methods "
 "approaches* (4th ed.). Sage Publications.",
 "Eisenhardt, K. M. (1989). Agency theory: An assessment and review. *Academy of Management "
 "Review, 14*(1), 57\u201374.",
 "Freeman, R. E. (1984). *Strategic management: A stakeholder approach*. Pitman.",
 "Herman, A. K. (2023). Factors influencing monitoring and evaluation planning on the performance "
 "of water supply projects in Dodoma City Council. *African Journal of Emerging Issues, 5*(17), "
 "104\u2013121.",
 "Ika, L. A. (2009). Project success as a topic in project management journals. *Project "
 "Management Journal, 40*(4), 6\u201319.",
 "Kacou, K. P., Ika, L. A., & Munro, L. T. (2022). Fifty years of capacity building: Taking stock "
 "and moving research forward. *Public Administration and Development, 42*(4), 215\u2013232. "
 "https://doi.org/10.1002/pad.1993",
 "Katerengabo, B., Gakuu, C., & Kidombo, H. (2023). Implementing project monitoring and evaluation "
 "plan with beneficiaries for improving performance: Evidence from Tanzania Conditional Cash "
 "Transfer. *International Journal of Sustainable Development Research, 9*(1), 11\u201317. "
 "https://doi.org/10.11648/j.ijsdr.20230901.12",
 "Killo, P. N. (2022). *Influence of monitoring and evaluation practices on performance of tobacco "
 "contract farming projects in Katavi Region, Tanzania* [Doctoral dissertation, The Open "
 "University of Tanzania].",
 "Kusek, J. Z., & Rist, R. C. (2004). *Ten steps to a results-based monitoring and evaluation "
 "system: A handbook for development practitioners*. World Bank.",
 "Kwareh, K. R., Mgale, Y. J., & Rwela, T. G. (2024). Influence of monitoring and evaluation "
 "practices on performance of health projects: Evidence from SIKIKA project in Dodoma and Dar es "
 "Salaam, Tanzania. *Open Access Library Journal, 11*(6), e11470. "
 "https://doi.org/10.4236/oalib.1111470",
 "Lushoto District Council. (2015). *District strategic plan 2015/16\u20132019/20*.",
 "Mabizela, H., & Zwane, Z. (2023). Monitoring and evaluation as critical approach to enhance the "
 "performance of local government: South Africa. *International Journal of Research in Business "
 "and Social Science, 12*(7), 74\u201384. https://doi.org/10.20525/ijrbs.v12i7.2746",
 "Masvaure, S., & Fish, T. E. (2022). Strengthening and measuring monitoring and evaluation "
 "capacity in selected African programmes. *African Evaluation Journal, 10*(1), a635. "
 "https://doi.org/10.4102/aej.v10i1.635",
 "Mgoba, S. A., & Kabote, S. J. (2020). Effectiveness of participatory monitoring and evaluation "
 "on achievement of community-based water projects in Tanzania. *Applied Water Science, 10*, "
 "Article 200.",
 "Mwaijande, F., Kengera, Z., & Nguliki, I. M. (2026). Evaluation in Tanzania. In R. Stockmann, "
 "W. Meyer, & T. Stockmann (Eds.), *The institutionalisation of evaluation in Africa* (pp. "
 "255\u2013285). Palgrave Macmillan. https://doi.org/10.1007/978-3-032-06301-4_10",
 "National Bureau of Statistics. (2022). *The 2022 population and housing census: Administrative "
 "units population distribution report*.",
 "Ochen-Ochen, I. (2025). The politics of monitoring and evaluation: Implications for evidence "
 "generation and use. *African Evaluation Journal, 13*(1), a792. "
 "https://doi.org/10.4102/aej.v13i1.792",
 "Office of the Controller and Auditor General. (2026). *Media statement on the annual general "
 "reports of the Controller and Auditor General, 14 April 2026*. National Audit Office of "
 "Tanzania. https://www.nao.go.tz/uploads/Media_Statement_-_English.pdf",
 "Organisation for Economic Co-operation and Development. (2010). *Glossary of key terms in "
 "evaluation and results based management* (2nd ed.). OECD Publishing.",
 "Rugeiyamu, R. (2024). Implementation of Tanzania\u2019s Development Vision 2025: Local government "
 "authorities\u2019 endeavours and challenges. *Commonwealth Journal of Local Governance, 29*, "
 "113\u2013129. https://doi.org/10.5130/cjlg.vi29.8443",
 "United Republic of Tanzania. (1982). *The Local Government (District Authorities) Act No. 7 of "
 "1982*. Government Printer.",
 "United Republic of Tanzania. (2000). *National policy on decentralisation by devolution*. "
 "President\u2019s Office \u2013 Regional Administration and Local Government.",
 "United Republic of Tanzania. (2021). *National Five Year Development Plan FYDP III "
 "2021/22\u20132025/26: Realising competitiveness and industrialisation for human development*. "
 "Ministry of Finance and Planning.",
 "Yamane, T. (1967). *Statistics: An introductory analysis* (2nd ed.). Harper and Row.",
]

# Ordered structure: (level, heading) then its paragraphs / tables
STRUCTURE = [
 ('h1', 'CHAPTER ONE: INTRODUCTION'),
 ('h2', '1.1 Background of the Study'),
 ('h2', '1.2 Statement of the Problem'),
 ('h2', '1.3 Justification of the Study'),
 ('h2', '1.4 Objectives of the Study'),
 ('h2', '1.5 Research Questions and Hypotheses'),
 ('h2', '1.6 Scope and Limitations of the Study'),
 ('h2', '1.7 Conceptual Framework'),
 ('caption', 'Figure 1: Conceptual framework of the study'),
 ('table', FIGURE1),
 ('source', 'Source: Author (2026)'),
 ('h2', '1.8 Ethical Considerations'),
 ('h1', 'CHAPTER TWO: REVIEW OF RELATED LITERATURE'),
 ('h2', '2.1 Introduction'),
 ('h2', '2.2 Theoretical Literature'),
 ('h2', '2.3 Empirical Literature'),
 ('h2', '2.4 Policy Review'),
 ('h1', 'CHAPTER THREE: METHODOLOGY'),
 ('h2', '3.1 Introduction'),
 ('h2', '3.2 Research Design'),
 ('h2', '3.3 Study Area'),
 ('h2', '3.4 Study Population'),
 ('h2', '3.5 Sample Size'),
 ('caption', 'Table 1: Target population and sample size distribution'),
 ('table', TABLE1),
 ('source', "Source: Author (2026), compiled from council records and computed using the Yamane "
            "formula"),
 ('h2', '3.6 Sampling Procedure'),
 ('h2', '3.7 Methods of Data Collection'),
 ('h2', '3.8 Data Analysis'),
 ('h2', '3.9 Ethical Considerations'),
 ('h1', '4.0 RESEARCH BUDGET'),
 ('caption', 'Table 2: Research budget'),
 ('table', TABLE2),
 ('source', 'Source: Author (2026)'),
 ('h1', '5.0 RESEARCH ACTION PLAN'),
 ('caption', 'Table 3: Research action plan'),
 ('table', TABLE3),
 ('source', 'Source: Author (2026)'),
 ('h1', 'REFERENCES'),
]

# 2.2 has two third-level headings; 1.4 has two as well
SUBHEADS = {
 '2.2 Theoretical Literature': ['2.2.1 Key Concepts', '2.2.2 Theories Guiding the Study'],
}


def typo(text):
    """Typography: a spaced hyphen becomes an en dash (used for parenthetical
    asides such as the project examples in 1.2 and the descriptive statistics in
    3.8). Applied inside q(), so every emitted string is treated consistently."""
    return text.replace(' - ', ' \u2013 ')


def q(text, indent='  '):
    """Emit a python string literal split over lines.

    Line wrapping keeps the trailing space on every wrapped line so that no
    word can be silently joined to the next one (a bug that corrupted an
    earlier draft). Text is passed through typo() first.
    """
    text = typo(text)
    words = text.split(' ')
    lines, cur = [], ''
    for w in words:
        if len(cur) + len(w) + 1 > 84:
            lines.append(cur + ' ')
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        lines.append(cur)
    out = []
    for i, ln in enumerate(lines):
        suffix = '' if i == len(lines) - 1 else ' '
        out.append('%s"%s"%s' % (indent, ln.replace('"', '\\"'), suffix))
    return '\n'.join(out)


buf = []
buf.append('# -*- coding: utf-8 -*-\n')
buf.append('"""\nContent of the research proposal, structured strictly per the TICD (Department '
           'of\nPostgraduate Studies, Research and Consultancy) "Research Proposal / Dissertation\n'
           'Writing Guidelines", April 2019 - Part A, 3.1.1 to 3.1.5.\n\nGuide constraints '
           'honoured: chapters 1-3 only (plus the research budget and action\nplan of 3.1.4 and '
           '3.1.5); future tense; 15-20 pages; 20-25 literature sources; APA\nauthor-date '
           'citation; British English.\n"""\n\n')
buf.append('TITLE = (\n%s)\n\n' % q('THE IMPACT OF MONITORING AND EVALUATION SYSTEM ON '
                                     'PERFORMANCE OF LOCAL GOVERNMENT PROJECTS IN LUSHOTO '
                                     'DISTRICT, TANGA REGION'))
buf.append('BLOCKS = []\n\n')
buf.append('def h1(t): BLOCKS.append(("h1", t))\n'
           'def h2(t): BLOCKS.append(("h2", t))\n'
           'def h3(t): BLOCKS.append(("h3", t))\n'
           'def p(t):  BLOCKS.append(("p", t))\n'
           'def ref(t): BLOCKS.append(("ref", t))\n'
           'def caption(t): BLOCKS.append(("caption", t))\n'
           'def source(t): BLOCKS.append(("source", t))\n'
           'def table(rows, widths=None, header=True, merge=False):\n'
           '    BLOCKS.append(("table", {"rows": rows, "widths": widths, "header": header, '
           '"merge": merge}))\n'
           'def pagebreak(): BLOCKS.append(("pagebreak", None))\n\n'
           'pagebreak()   # the title page is generated separately by the builder\n\n')

pending_h3 = None
for level, item in STRUCTURE:
    if level in ('h1',):
        buf.append('h1(%s)\n\n' % q(item)[2:])
        continue
    if level == 'h2':
        buf.append('h2(%s)\n' % q(item)[2:])
        if item == '1.4 Objectives of the Study':
            for sub, paras in KEEP[item]['h3']:
                buf.append('h3(%s)\n' % q(sub)[2:])
                for para in paras:
                    buf.append('p(%s)\n' % q(para)[2:])
            buf.append('\n')
            continue
        if item == '4.0 RESEARCH BUDGET' or item == '5.0 RESEARCH ACTION PLAN':
            pass
        if item in SUBHEADS:
            subs = SUBHEADS[item]
            paras = NEW[item]
            # first paragraph -> first sub-heading, rest -> second
            buf.append('h3(%s)\n' % q(subs[0])[2:])
            buf.append('p(%s)\n' % q(paras[0])[2:])
            buf.append('h3(%s)\n' % q(subs[1])[2:])
            for para in paras[1:]:
                buf.append('p(%s)\n' % q(para)[2:])
            buf.append('\n')
            continue
        paras = NEW.get(item) or KEEP.get(item, {}).get('paras', [])
        for para in paras:
            buf.append('p(%s)\n' % q(para)[2:])
        buf.append('\n')
        continue
    if level == 'h1x':
        continue
    if level == 'caption':
        buf.append('caption(%s)\n' % q(item)[2:])
        continue
    if level == 'source':
        buf.append('source(%s)\n\n' % q(item)[2:])
        continue
    if level == 'table':
        rows, widths, header, merge = item
        buf.append('table(\n')
        buf.append(pprint.pformat(rows, width=96, indent=4).replace('\n', '\n') + ',\n')
        buf.append('      widths=%r, header=%r, merge=%r)\n\n' % (widths, header, merge))
        continue

# budget / action plan h1 sections need their intro paragraph after the heading
text = ''.join(buf)
text = text.replace('h1("4.0 RESEARCH BUDGET")\n\n',
                    'h1("4.0 RESEARCH BUDGET")\n' +
                    '\n'.join('p(%s)' % q(x)[2:] for x in KEEP['4.0 RESEARCH BUDGET']['paras']) +
                    '\n\n')
text = text.replace('h1("5.0 RESEARCH ACTION PLAN")\n\n',
                    'h1("5.0 RESEARCH ACTION PLAN")\n' +
                    '\n'.join('p(%s)' % q(x)[2:] for x in KEEP['5.0 RESEARCH ACTION PLAN']['paras']) +
                    '\n\n')

buf = [text]
buf.append('REFERENCES = [\n')
for r in REFERENCES:
    buf.append(q(r, indent=' ') + ',\n\n')
buf.append(']\n')
buf.append('for r in REFERENCES:\n    ref(r)\n')

open('proposal_content.py', 'w', encoding='utf-8').write(''.join(buf))
print('written proposal_content.py')
