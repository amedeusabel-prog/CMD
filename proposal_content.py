# -*- coding: utf-8 -*-
"""
Content of the research proposal, structured strictly per the TICD (Department of
Postgraduate Studies, Research and Consultancy) "Research Proposal / Dissertation
Writing Guidelines", April 2019 - Part A, 3.1.1 to 3.1.5.

Guide constraints honoured: chapters 1-3 only (plus the research budget and action
plan of 3.1.4 and 3.1.5); future tense; 15-20 pages; 20-25 literature sources; APA
author-date citation; British English.
"""

TITLE = (
  "THE IMPACT OF MONITORING AND EVALUATION SYSTEM ON PERFORMANCE OF LOCAL GOVERNMENT " 
  "PROJECTS IN LUSHOTO DISTRICT, TANGA REGION")

BLOCKS = []

def h1(t): BLOCKS.append(("h1", t))
def h2(t): BLOCKS.append(("h2", t))
def h3(t): BLOCKS.append(("h3", t))
def p(t):  BLOCKS.append(("p", t))
def ref(t): BLOCKS.append(("ref", t))
def caption(t): BLOCKS.append(("caption", t))
def source(t): BLOCKS.append(("source", t))
def table(rows, widths=None, header=True, merge=False):
    BLOCKS.append(("table", {"rows": rows, "widths": widths, "header": header, "merge": merge}))
def pagebreak(): BLOCKS.append(("pagebreak", None))

pagebreak()   # the title page is generated separately by the builder

h1("CHAPTER ONE: INTRODUCTION")

h2("1.1 Background of the Study")
p("Public investment in local infrastructure is how devolved governments convert public " 
  "resources into services. Whether such investment is completed on schedule, within " 
  "budget, to technical standard and put to sustained use depends largely on the " 
  "quality of the accompanying monitoring and evaluation (M&E) system, which combines " 
  "the institutions, human resources, indicators, tools and mechanisms for using " 
  "information in decision making (Kusek and Rist, 2004).")
p("Results-based management has become the dominant global paradigm, moving governments " 
  "from measuring inputs to measuring results and correcting deviations before they " 
  "become losses (Kusek and Rist, 2004; OECD, 2010). In sub-Saharan Africa devolution " 
  "has shifted service delivery to local governments with fragile M&E structures: Okeyo " 
  "*et al.* (2019) found that Kenyan county organograms provided no M&E offices, and " 
  "Chebet Murei *et al.* (2017) that M&E human resource capacity determined the " 
  "performance of horticulture projects in Nakuru County.")
p("In Tanzania, Decentralisation by Devolution (D by D) was adopted in 2000 to bring " 
  "decision making, resources and services closer to the people (United Republic of " 
  "Tanzania [URT], 2000). Under the Local Government (District Authorities) Act No. 7 " 
  "of 1982 district councils plan, implement, supervise and evaluate local projects " 
  "(URT, 1982), while PO-RALG provides oversight. Audit evidence shows persistent " 
  "weakness: in the reports tabled in April 2026 the Controller and Auditor General " 
  "found that only 36.7% of the 38,181 recommendations issued in previous years had " 
  "been implemented and that local government authorities (LGAs) continued to record " 
  "delayed projects, payments for incomplete works, weak contract management and " 
  "inadequate supervision (Office of the Controller and Auditor General [CAG], 2026). " 
  "Tanzanian studies attribute such outcomes to weak M&E plans, unskilled staff and " 
  "political interference (Mhina, 2017; Maimula, 2017), while Herman (2023) and Killo " 
  "(2022) respectively confirmed the significance of M&E planning for water projects in " 
  "Dodoma City Council and of M&E human resource capacity and stakeholder involvement " 
  "for projects in Katavi Region.")
p("Lushoto District Council is one of the eleven LGAs of Tanga Region. It covers 3,297 " 
  "square kilometres in the Usambara Mountains and had 350,958 residents in the 2022 " 
  "census (National Bureau of Statistics [NBS], 2022); the 2012 census recorded 332,436 " 
  "people, of whom 153,847 (46.3%) were men and 178,589 (53.7%) were women, in 71,009 " 
  "households, 71.4% of them in villages (Lushoto District Council, 2015). Its " 
  "Strategic Plan for 2015/16-2019/20 prioritised health, water, education and road " 
  "infrastructure and set a target of raising management and governance systems from " 
  "55% to 60%, financing coming mainly through earmarked central grants and own-source " 
  "revenue (Lyon *et al.*, 2017). Council reports indicate time and cost overruns, " 
  "stalled works and participation confined to project identification.")

h2("1.2 Statement of the Problem")
p("Ideally, Lushoto District Council should deliver its projects – water schemes, " 
  "classrooms, health facilities, roads and markets – on schedule, within budget and to " 
  "technical standards, with completed facilities used and maintained by beneficiaries. " 
  "That requires a functioning M&E system: an approved plan with baselines, indicators " 
  "and targets; qualified staff; and the systematic involvement of councillors, ward " 
  "and village authorities, contractors and beneficiaries in monitoring and in the use " 
  "of findings (URT, 2000).")
p("In reality, council projects record delays, cost overruns, substandard or abandoned " 
  "works and low post-completion utilisation. Audit reports tabled in April 2026 show " 
  "that only 36.7% of 38,181 previous recommendations had been implemented and that " 
  "LGAs recorded delayed projects, payments for incomplete works and weak contract " 
  "management (CAG, 2026), outcomes attributed to weak M&E planning, untrained M&E " 
  "human resources and the exclusion of stakeholders from M&E (Mhina, 2017; Maimula, " 
  "2017; Herman, 2023; Killo, 2022). In Lushoto the M&E function is coordinated through " 
  "the planning structure while sector departments supervise projects, and " 
  "participation is largely limited to project identification, yet no systematic study " 
  "has quantified how much of this deficit is explained by M&E planning practices, M&E " 
  "human resource capacity and stakeholder involvement in M&E.")
p("If the situation persists, public resources will keep being committed to projects " 
  "delivered late, at higher cost and of questionable quality, undermining the " 
  "Council's ability to meet national plan targets (URT, 2021) and its own strategic " 
  "plan objectives, weakening citizen confidence in devolved government and " 
  "perpetuating service gaps for the district's 350,958 residents (NBS, 2022), a large " 
  "proportion of whom are women and children in rural wards. The study will therefore " 
  "assess the impact of the M&E system on the performance of local government projects " 
  "in Lushoto District Council.")

h2("1.3 Justification of the Study")
p("The study will convert a generalised concern about poor project delivery into " 
  "measurable evidence on three M&E dimensions that council management can act upon. " 
  "The management team, planning and sector departments and the internal audit unit " 
  "will learn where M&E planning, staffing and participation require strengthening and " 
  "will gain a basis for answering audit recommendations. PO-RALG and the Tanga " 
  "Regional Secretariat will obtain evidence for targeting capacity building and " 
  "oversight to rural councils. Citizens, ward and village authorities and project " 
  "committees will benefit from improved transparency, ownership and value for money. " 
  "Academically, the study will fill a contextual gap, since most Tanzanian evidence " 
  "comes from cities, non-governmental organisations or single sectors rather than from " 
  "a rural mountain council, and it will test agency and stakeholder propositions in a " 
  "devolved setting.")

h2("1.4 Objectives of the Study")
h3("1.4.1 General Objective")
p("To assess the impact of the monitoring and evaluation system on the performance of " 
  "local government projects in Lushoto District, Tanga Region.")
h3("1.4.2 Specific Objectives")
p("(i) To examine the extent to which M&E planning practices influence the performance " 
  "of local government projects in Lushoto District; (ii) to assess the influence of " 
  "M&E human resource capacity on the performance of local government projects in " 
  "Lushoto District; and (iii) to determine the influence of stakeholder involvement in " 
  "M&E on the performance of local government projects in Lushoto District.")

h2("1.5 Research Questions and Hypotheses")
p("Because the study will use a mixed-methods design, research questions will guide all " 
  "three objectives while the corresponding hypotheses will be tested on the " 
  "quantitative strand. RQ1: to what extent do M&E planning practices influence the " 
  "performance of local government projects in Lushoto District? RQ2: how does M&E " 
  "human resource capacity influence that performance? RQ3: to what extent does " 
  "stakeholder involvement in M&E influence that performance?")
p("H01: M&E planning practices have no significant influence on the performance of " 
  "local government projects in Lushoto District (H11: they have a significant positive " 
  "influence). H02: M&E human resource capacity has no significant influence on that " 
  "performance (H12: it has a significant positive influence). H03: stakeholder " 
  "involvement in M&E has no significant influence on that performance (H13: it has a " 
  "significant positive influence).")

h2("1.6 Scope and Limitations of the Study")
p("In content the study will be confined to the three specific objectives and to " 
  "project performance measured through timeliness, cost efficiency, technical quality, " 
  "utilisation and sustainability, and beneficiary satisfaction. Geographically it will " 
  "cover Lushoto District Council in eight purposively selected wards, and " 
  "substantively it will cover water, education, health, roads and markets projects " 
  "implemented in the five financial years from 2021/22 to 2025/26, whether completed, " 
  "ongoing or stalled.")
p("Four limitations are anticipated and will be curbed as follows: reluctance of staff " 
  "and contractors to disclose information on delayed or defective projects, by " 
  "guaranteeing anonymity and presenting an introduction letter; recall bias on older " 
  "projects, by verifying responses against project files and site observation; " 
  "difficult terrain and poor feeder roads, by scheduling fieldwork in the dry months " 
  "and clustering wards; and non-response, by maintaining a 10% replacement reserve.")

h2("1.7 Conceptual Framework")
p("The framework is derived from the problem analysis and from results-based " 
  "management, agency and stakeholder theories. M&E planning practices are expected to " 
  "supply the indicators, baselines and targets against which progress is measured, M&E " 
  "human resource capacity to determine whether planned monitoring is executed " 
  "competently, and stakeholder involvement to improve the accuracy, legitimacy and use " 
  "of M&E information; together they will explain variation in project performance, " 
  "subject to the intervening conditions shown in Figure 1.")

caption("Figure 1: Conceptual framework of the study")
table(
[   ['INDEPENDENT VARIABLES', '', ''],
    [   'M&E planning practices\n'
        '- M&E plans\n'
        '- baselines, indicators, targets\n'
        '- budget, tools, schedules',
        'M&E human resource capacity\n'
        '- number of M&E staff\n'
        '- qualifications and training\n'
        '- experience and analysis skills',
        'Stakeholder involvement in M&E\n'
        '- beneficiaries and community\n'
        '- ward and village committees\n'
        '- contractors, PO-RALG, partners'],
    ['↓', '', ''],
    [   'INTERVENING VARIABLES: timely release of funds; political will; legal and '
        'institutional framework; project complexity; M&E information systems',
        '',
        ''],
    ['↓', '', ''],
    [   'DEPENDENT VARIABLE - Performance of local government projects: completion within '
        'schedule and budget; technical quality; utilisation and sustainability; beneficiary '
        'satisfaction',
        '',
        '']],
      widths=[4.9, 4.7, 4.8], header=False, merge=True)

source("Source: Author (2026)")

h2("1.8 Ethical Considerations")
p("Before fieldwork the researcher will obtain a letter of introduction from the " 
  "Institute and research permission from PO-RALG, the Tanga Regional Commissioner, the " 
  "Lushoto District Commissioner and the Council Director. Participation will be " 
  "voluntary and based on informed consent; anonymity and confidentiality will be " 
  "guaranteed by omitting names, coding responses and restricting access to data, which " 
  "will be used solely for academic purposes. No fabricated or plagiarised material " 
  "will be presented, and findings will be reported back to the Council.")

h1("CHAPTER TWO: REVIEW OF RELATED LITERATURE")

h2("2.1 Introduction")
p("This chapter reviews the literature giving the study its theoretical basis, " 
  "organised into theoretical literature, empirical literature and policy review, and " 
  "ends with the gaps the study will address.")

h2("2.2 Theoretical Literature")
h3("2.2.1 Key Concepts")
p("Monitoring is the continuous collection of data on specified indicators to show " 
  "progress and the use of funds; evaluation is the systematic assessment of a project " 
  "against relevance, efficiency, effectiveness, impact and sustainability (OECD, " 
  "2010). An M&E system combines the indicators, methods, institutions and processes " 
  "through which an organisation tracks implementation and assesses results (Kusek and " 
  "Rist, 2004). M&E planning practices are the front-end design of that function: the " 
  "plan, baselines, indicators, targets, tools and budget (Herman, 2023). M&E human " 
  "resource capacity is the number, qualifications, training, experience and analytical " 
  "skill of M&E staff at individual, organisational and enabling-environment levels " 
  "(Mackay, 2007; Chebet Murei *et al.*, 2017). Stakeholder involvement in M&E is the " 
  "participation of beneficiaries, elected leaders, contractors and oversight bodies in " 
  "data collection, joint site visits and corrective decisions (Mgoba and Kabote, " 
  "2020). Project performance is accomplishment against schedule, cost and quality, " 
  "extended to strategic criteria, stakeholder satisfaction and sustainability (Ika, " 
  "2009), and local government projects are investments planned, financed, procured and " 
  "supervised by a council under the Local Government (District Authorities) Act No. 7 " 
  "of 1982 (URT, 1982).")
h3("2.2.2 Theories Guiding the Study")
p("Results-based management shifts attention from inputs to outputs, outcomes and " 
  "impact and treats the M&E plan, indicators and use of information as the engine of " 
  "that shift (Kusek and Rist, 2004; OECD, 2010); it underpins the first objective. " 
  "Agency theory explains why planning alone is insufficient: each agent in the chain " 
  "from citizens through the council to contractors holds more information than the " 
  "principal and may pursue its own interest, so monitoring reduces information " 
  "asymmetry and agency costs, and the competence of the monitor determines how well it " 
  "works (Eisenhardt, 1989); this anchors the second objective. Stakeholder theory " 
  "holds that an organisation must manage the interests of all groups that affect or " 
  "are affected by its activities, and that their involvement improves the legitimacy, " 
  "accuracy and use of information (Freeman, 1984); it anchors the third objective, and " 
  "beneficiaries' participation yields information outsiders cannot obtain (Mgoba and " 
  "Kabote, 2020). Evaluation capacity theory adds that capacity must be matched by " 
  "demand for information (Mackay, 2007). The study will be anchored on agency and " 
  "stakeholder theories, complemented by results-based management and evaluation " 
  "capacity.")

h2("2.3 Empirical Literature")
p("On M&E planning, Herman (2023) used a mixed-methods design with 170 respondents " 
  "selected by the Yamane formula and found that M&E planning significantly affected " 
  "the performance of water supply projects in Dodoma City Council (p < 0.05); Mhina " 
  "(2017) reported weak M&E plans, unskilled staff and limited use of reports in Ruvuma " 
  "district councils; and Okeyo *et al.* (2019) found M&E structure, process, method " 
  "and policy to be significant predictors of county project performance in six Kenyan " 
  "counties (F change = 109.403, p < 0.05).")
p("On M&E human resource capacity, Chebet Murei *et al.* (2017) established that M&E " 
  "human resource capacity influenced the performance of horticulture projects in " 
  "Nakuru County; Maimula (2017) found that local government water projects in Mkuranga " 
  "suffered from political interference, weak M&E teams and unqualified technical " 
  "staff; and Killo (2022) identified M&E human resource capacity and technical " 
  "expertise among the strongest influences on project performance in Katavi Region. " 
  "Capacity is however often proxied by training attendance rather than by competence " 
  "in indicator design and analysis.")
p("On stakeholder involvement, Mgoba and Kabote (2020) demonstrated that participatory " 
  "M&E significantly improved the achievement of community-based water projects in " 
  "Tanzania, and Katerengabo *et al.* (2023), using 400 household heads, found that " 
  "households' involvement in implementing the M&E plan significantly influenced the " 
  "performance of the Tanzania Conditional Cash Transfer project (t = 8.472, p < " 
  "0.001). These studies concern community-managed projects rather than council capital " 
  "projects, and measure involvement as meeting attendance rather than influence over " 
  "monitoring decisions.")
p("Four gaps emerge. Contextually, no published study examines the impact of the M&E " 
  "system on the performance of local government projects in Lushoto District or in any " 
  "council of Tanga Region. Conceptually, M&E is usually treated as one composite " 
  "variable, leaving the separate contributions of planning, human resource capacity " 
  "and stakeholder involvement unquantified, and performance is often measured by " 
  "perception rather than by schedule, cost and quality. Methodologically, most studies " 
  "are single-method surveys whose results cannot be verified against project records " 
  "or physical works. The study will address these gaps by disaggregating the M&E " 
  "system into three measurable dimensions, measuring performance on five indicators " 
  "verified through documents and site observation, and combining regression with " 
  "qualitative enquiry in one council.")

h2("2.4 Policy Review")
p("The National Policy on Decentralisation by Devolution requires councils to plan, " 
  "implement and account for local development, with PO-RALG providing oversight (URT, " 
  "2000), and the Local Government (District Authorities) Act No. 7 of 1982 confers the " 
  "council's mandate over local services and projects (URT, 1982). The PO-RALG " 
  "assessment of D by D implementation found a shift of powers to regions and sector " 
  "ministries, heavy dependence on earmarked transfers and weakened local oversight, " 
  "which constrain a council's ability to monitor and correct its own projects (Lyon " 
  "*et al.*, 2017). The Third National Five Year Development Plan for 2021/22-2025/26 " 
  "commits government to strengthening implementation, monitoring and evaluation (URT, " 
  "2021), while the audit reports tabled in April 2026 recommend stronger management of " 
  "public projects so that they are delivered on time, meet quality standards and " 
  "remain within controlled costs (CAG, 2026). At local level, the Lushoto District " 
  "Council Strategic Plan for 2015/16-2019/20 contains a monitoring and assessment " 
  "component and sets sector targets including the improvement of management and " 
  "governance systems, providing the local policy basis for examining M&E arrangements " 
  "and project performance (Lushoto District Council, 2015).")

h1("CHAPTER THREE: METHODOLOGY")

h2("3.1 Introduction")
p("This chapter describes the research design, study area, study population, sample " 
  "size, sampling procedure, methods of data collection, data analysis and ethical " 
  "considerations, with the reason for each choice supported by methodological " 
  "literature.")

h2("3.2 Research Design")
p("The study will adopt an explanatory sequential mixed-methods design embedded in a " 
  "cross-sectional survey and a single case study of Lushoto District Council. The " 
  "quantitative strand will be conducted first through a survey of M&E stakeholders, " 
  "and the qualitative strand will follow through key informant interviews, focus group " 
  "discussions, document review and site observation to explain the results. Mixed " 
  "methods are chosen because M&E performance questions involve both measurable " 
  "relationships and context-specific explanations, and because combining survey, " 
  "qualitative and documentary evidence increases validity in development settings " 
  "(Creswell, 2014).")

h2("3.3 Study Area")
p("The study will be conducted in Lushoto District Council of Tanga Region, in the " 
  "Usambara Mountains, covering 3,297 square kilometres and bordered by Kenya, Muheza, " 
  "Korogwe and Bumbuli Districts and Kilimanjaro Region, with Lushoto town as its " 
  "headquarters; it had 350,958 residents in 2022 (NBS, 2022). The economy is dominated " 
  "by smallholder horticulture, dairy, forestry and tourism, and the council implements " 
  "a large portfolio of water, classroom, health facility, road and market projects. " 
  "Lushoto was chosen because it is a typical rural mountain council with a diverse " 
  "project portfolio whose strategic plan sets explicit monitoring and governance " 
  "targets, because reported delays and under-utilisation make it an information-rich " 
  "case, and because the researcher's familiarity with the area eases entry.")

h2("3.4 Study Population")
p("The study population will comprise all categories of persons who plan, execute, " 
  "supervise, finance, benefit from or oversee the M&E of council projects. The " 
  "estimated target population of 1,087 individuals was derived from council " 
  "establishment records, ward and village committee registers and the contractors' " 
  "register, and will be confirmed with the Council at the entry meeting.")

h2("3.5 Sample Size")
p("The sample size will be determined using the Yamane formula, n = N/(1 + Ne²), where " 
  "N is the target population and e is the precision level of 0.05 at 95% confidence " 
  "(Yamane, 1967). With N = 1,087, n = 1,087/(1 + 1,087 × 0.0025) = 293 respondents. " 
  "The formula is chosen because the population is finite and its size is known from " 
  "council records, and a reserve of 10% (29 respondents) will be drawn from the same " 
  "strata to replace non-responses. In addition, 12 key informants will be interviewed, " 
  "four focus group discussions of eight to ten participants each will be held, and 12 " 
  "project sites will be observed. Table 1 shows the population and the proportional " 
  "allocation of the sample.")

caption("Table 1: Target population and sample size distribution")
table(
[   ['S/No', 'Category of respondents', 'N', 'n'],
    ['1', 'Council management team and heads of departments', '26', '7'],
    ['2', 'Planning and M&E unit staff and sector M&E focal persons', '34', '9'],
    ['3', 'Technical staff of implementing departments', '145', '39'],
    ['4', 'Ward Executive Officers and ward councillors', '56', '16'],
    ['5', 'Ward development committee members', '168', '45'],
    ['6', 'Village Executive Officers and village chairpersons', '210', '56'],
    ['7', 'Project and facility committee members', '385', '104'],
    ['8', "Contractors' and consultants' site personnel", '63', '17'],
    ['', 'Total', '1,087', '293']],
      widths=[1.1, 9.1, 2.1, 2.1], header=True, merge=False)

source("Source: Author (2026), compiled from council records and computed using the Yamane " 
  "formula")

h2("3.6 Sampling Procedure")
p("A multistage procedure will be used. First, eight wards will be selected purposively " 
  "on the basis of project portfolio size, the presence of completed and ongoing or " 
  "stalled projects, and geographic spread across the lowland and mountain zones. " 
  "Second, respondents will be stratified by the categories in Table 1 and the sample " 
  "allocated proportionally. Third, individuals will be drawn from the council staff " 
  "list, the ward and village committee registers and the contractors' register by " 
  "simple random sampling using computer-generated random numbers. Fourth, key " 
  "informants will be selected purposively: the Council Director, the planning and M&E " 
  "officer, the heads of the works, health, education and water departments, the " 
  "internal auditor, two contractors and one development partner representative. " 
  "Project sites will be purposively selected to cover the five sub-sectors and three " 
  "implementation statuses.")

h2("3.7 Methods of Data Collection")
p("Both primary and secondary data will be collected. Primary quantitative data will be " 
  "collected through a structured questionnaire with closed-ended items on a five-point " 
  "Likert scale covering the three M&E dimensions and project performance; the " 
  "questionnaire is preferred because it reaches a large, dispersed sample at low cost " 
  "and yields standardised data suitable for regression. Primary qualitative data will " 
  "be collected through semi-structured interview guides for key informants and focus " 
  "group discussion guides for ward and village project committees and beneficiaries, " 
  "which allow probing of why projects are delayed and how M&E information is used. An " 
  "observation checklist will be used at the 12 sites to verify physical progress, " 
  "workmanship and utilisation, and a document review checklist will cover the Council " 
  "Strategic Plan, implementation reports, project M&E plans and files, payment " 
  "records, council minutes and audit reports; triangulation across these sources will " 
  "strengthen validity (Creswell, 2014).")
p("The instruments will be pilot tested with 30 respondents in a comparable council " 
  "outside the study sample to check clarity, length and sequencing. Content validity " 
  "will be secured by having the supervisor and two M&E practitioners review the " 
  "instruments against the objectives, and reliability will be assessed with Cronbach's " 
  "alpha, a coefficient of 0.70 or above being acceptable.")

h2("3.8 Data Analysis")
p("Quantitative data will be cleaned, coded and entered into the Statistical Package " 
  "for the Social Sciences (SPSS) Version 27. Descriptive statistics – frequencies, " 
  "percentages, means and standard deviations – will summarise respondent profiles and " 
  "the level of each variable. Inferential analysis will use Pearson correlation for " 
  "bivariate relationships and multiple linear regression to test the influence of the " 
  "three M&E dimensions on project performance using the model PP = β₀ + β₁MPP + β₂MHC " 
  "+ β₃SI + ε, where PP is project performance, MPP is M&E planning practices, MHC is " 
  "M&E human resource capacity, SI is stakeholder involvement in M&E, β₁ to β₃ are the " 
  "coefficients and ε is the error term. Composite scores will be generated from the " 
  "Likert items of each construct, assumptions will be tested for normality, " 
  "multicollinearity (variance inflation factor below 10) and homoscedasticity, and " 
  "hypotheses will be tested at a 5% significance level. Qualitative data will be " 
  "transcribed, coded and analysed thematically against the specific objectives, and " 
  "the two strands will then be integrated through triangulation.")

h2("3.9 Ethical Considerations")
p("The study will comply with the requirements set out in section 1.8: an introduction " 
  "letter and research permission from PO-RALG, the Regional Commissioner, the District " 
  "Commissioner and the Council Director will be obtained before data collection; " 
  "informed consent will be sought from every respondent; anonymity will be protected " 
  "by coding questionnaires; confidentiality will be maintained by reporting results in " 
  "aggregate form so that no individual or contract can be identified; and the " 
  "researcher will avoid fabrication, falsification and plagiarism.")

h1("4.0 RESEARCH BUDGET")
p("The tentative budget below covers the items and services required to implement the " 
  "study. Funds will come from the researcher's personal savings, with supplementary " 
  "support from the Institute where available.")

caption("Table 2: Research budget")
table(
[   ['S/No', 'Item / service', 'Quantity', 'Unit cost (TZS)', 'Total (TZS)'],
    ['1', 'Stationery, printing and photocopying', 'Lump sum', '-', '450,000'],
    [   '2',
        'Questionnaire administration (2 assistants, 14 days)',
        '28 days',
        '40,000',
        '1,120,000'],
    ['3', 'Field transport within the district', '14 days', '65,000', '910,000'],
    ['4', 'Travel to and from the study area', '4 trips', '120,000', '480,000'],
    ['5', 'Subsistence and accommodation', '28 days', '70,000', '1,960,000'],
    ['6', 'Pilot study', '30', '10,000', '300,000'],
    [   '7',
        'Data analysis, statistical consultation and communication',
        'Lump sum',
        '-',
        '750,000'],
    ['8', 'Printing, binding and defence logistics', 'Lump sum', '-', '600,000'],
    ['', 'Sub-total', '', '', '6,570,000'],
    ['', 'Contingency at 10%', '', '', '657,000'],
    ['', 'Grand total', '', '', '7,227,000']],
      widths=[1.1, 6.3, 2.4, 2.4, 2.6], header=True, merge=False)

source("Source: Author (2026)")

h1("5.0 RESEARCH ACTION PLAN")
p("The activities below will be undertaken in the sequence and periods indicated, " 
  "allowing for proposal defence, permits, pilot testing, fieldwork, analysis, report " 
  "writing and submission.")

caption("Table 3: Research action plan")
table(
[   ['S/No', 'Activity', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr'],
    ['1', 'Proposal writing and submission', 'X', '', '', '', '', '', '', ''],
    ['2', 'Proposal defence and corrections', '', 'X', '', '', '', '', '', ''],
    ['3', 'Clearance, permits and entry meetings', '', 'X', 'X', '', '', '', '', ''],
    ['4', 'Instrument development and pilot test', '', '', 'X', '', '', '', '', ''],
    ['5', 'Data collection in the field', '', '', '', 'X', 'X', '', '', ''],
    ['6', 'Data cleaning, coding and analysis', '', '', '', '', 'X', 'X', '', ''],
    ['7', 'Interpretation and report writing', '', '', '', '', '', 'X', 'X', ''],
    ['8', 'Draft submission, binding and final defence', '', '', '', '', '', '', 'X', 'X']],
      widths=[1.0, 6.6, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95], header=True, merge=False)

source("Source: Author (2026)")

h1("REFERENCES")

REFERENCES = [
 "Chebet Murei, M.L.; Kidombo, P.H.; Gakuu, P.C. (2017). Influence of monitoring and " 
 "evaluation human resources capacity on performance of horticulture projects in " 
 "Nakuru County, Kenya. *IJRDO – Journal of Social Science and Humanities Research* 2 " 
 "(11): 112-131.",

 "Creswell, J.W. (2014). *Research Design: Qualitative, Quantitative and Mixed Methods " 
 "Approaches*. (4th ed.). Sage Publications, Thousand Oaks, 296pp.",

 "Eisenhardt, K.M. (1989). Agency theory: an assessment and review. *Academy of " 
 "Management Review* 14 (1): 57-74.",

 "Freeman, R.E. (1984). *Strategic Management: A Stakeholder Approach*. Pitman, " 
 "Boston, 276pp.",

 "Herman, A.K. (2023). Factors influencing monitoring and evaluation planning on the " 
 "performance of water supply projects in Dodoma City Council. *African Journal of " 
 "Emerging Issues* 5 (17): 104-121.",

 "Ika, L.A. (2009). Project success as a topic in project management journals. " 
 "*Project Management Journal* 40 (4): 6-19.",

 "Katerengabo, B.; Gakuu, C.; Kidombo, H. (2023). Implementing project monitoring and " 
 "evaluation plan with beneficiaries for improving performance: evidence from Tanzania " 
 "Conditional Cash Transfer. *International Journal of Sustainable Development " 
 "Research* 9 (1): 11-17.",

 "Killo, P.N. (2022). *Influence of Monitoring and Evaluation Practices on Performance " 
 "of Tobacco Contract Farming Projects in Katavi Region, Tanzania*. Dissertation for " 
 "the Award of PhD Degree at The Open University of Tanzania, Dar es Salaam, Tanzania.",

 "Kusek, J.Z.; Rist, R.C. (2004). *Ten Steps to a Results-Based Monitoring and " 
 "Evaluation System: A Handbook for Development Practitioners*. World Bank, Washington " 
 "DC, 216pp.",

 "Lushoto District Council (2015). *District Council's Strategic Plan for the Period " 
 "2015-2020*. Lushoto District Council, Lushoto, Tanzania.",

 "Lyon, A.; Zilihona, I.; Masanyiwa, Z. (2017). *Report on Assessment of " 
 "Implementation of Decentralisation by Devolution in Tanzania*. President's Office – " 
 "Regional Administration and Local Government, Dodoma, Tanzania.",

 "Mackay, K. (2007). *Building Evaluation Capacity: Activities and Outcomes*. World " 
 "Bank, Washington DC, 232pp.",

 "Maimula, S. (2017). *Challenges in Practicing Monitoring and Evaluation: The Case of " 
 "Local Government Water Projects in Mkuranga, Tanzania*. Dissertation for the Award " 
 "of Master of Arts in Monitoring and Evaluation at The Open University of Tanzania, " 
 "Dar es Salaam, Tanzania, 105pp.",

 "Mgoba, S.A.; Kabote, S.J. (2020). Effectiveness of participatory monitoring and " 
 "evaluation on achievement of community-based water projects in Tanzania. *Applied " 
 "Water Science* 10: 200.",

 "Mhina, G. (2017). *Monitoring and Evaluation Practices and their Effects in District " 
 "Councils: A Case of Ruvuma Region*. Dissertation for the Award of Master's Degree at " 
 "Mzumbe University, Morogoro, Tanzania.",

 "National Bureau of Statistics (2022). *The 2022 Population and Housing Census: " 
 "Administrative Units Population Distribution Report*. National Bureau of Statistics, " 
 "Dodoma, Tanzania.",

 "Okeyo, E.O.; Mogusu, J.; Ombachi, N.K. (2019). Effectiveness of monitoring and " 
 "evaluation structure on the performance of county government projects in the Lake " 
 "Region Economic Bloc of Nyanza, Kenya. *International Journal of Scientific and " 
 "Research Publications* 9 (3): 691-699.",

 "Office of the Controller and Auditor General (2026). *Media Statement on the Annual " 
 "General Reports of the Controller and Auditor General, 14 April 2026*. National " 
 "Audit Office of Tanzania, Dodoma. " 
 "[https://www.nao.go.tz/uploads/Media_Statement_-_English.pdf] site visited on " 
 "16/9/2026.",

 "Organisation for Economic Co-operation and Development (2010). *Glossary of Key " 
 "Terms in Evaluation and Results Based Management*. (2nd ed.). OECD Publishing, " 
 "Paris, 46pp.",

 "United Republic of Tanzania (1982). *The Local Government (District Authorities) Act " 
 "No. 7 of 1982*. Government Printer, Dar es Salaam, Tanzania.",

 "United Republic of Tanzania (2000). *National Policy on Decentralisation by " 
 "Devolution*. President's Office – Regional Administration and Local Government, " 
 "Dodoma, Tanzania.",

 "United Republic of Tanzania (2021). *National Five Year Development Plan FYDP III " 
 "2021/22-2025/26: Realising Competitiveness and Industrialisation for Human " 
 "Development*. Ministry of Finance and Planning, Dodoma, Tanzania.",

 "Yamane, T. (1967). *Statistics: An Introductory Analysis*. (2nd ed.). Harper and " 
 "Row, New York, 919pp.",

]
for r in REFERENCES:
    ref(r)
