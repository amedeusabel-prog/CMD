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
p("Governments and development partners have placed monitoring and evaluation (M&E) at " 
  "the centre of public project management since the 1990s. Kusek and Rist (2004) " 
  "presented the results-based M&E system as the route through which a government " 
  "tracks implementation, learns from experience and improves the use of public " 
  "resources. Ba (2021) reported that the World Bank assessment of 2007 found little " 
  "effectiveness in such systems, and Kacou et al. (2022) concluded from fifty years of " 
  "capacity building research that a formal system alone does not produce results, " 
  "because context, demand and use determine performance. The global evidence therefore " 
  "shows that the presence of an M&E system does not guarantee project performance.")
p("Sub-Saharan Africa has supplied the clearest evidence of the gap between formal " 
  "systems and actual performance. Masvaure and Fish (2022) studied M&E capacity " 
  "strengthening in eight African countries, including Tanzania, and found that the " 
  "initiatives remained ad hoc and focused on individual skills rather than on " 
  "organisational systems. Mabizela and Zwane (2023) established in three South African " 
  "district municipalities that the absence of a functional M&E system contributed " 
  "directly to weak service delivery. Ochen-Ochen (2025) observed in Western Uganda " 
  "that M&E generated the evidence which donors required but produced little local use, " 
  "and that political leaders sought participation in monitoring for political capital. " 
  "African local governments therefore face institutional, human resource and political " 
  "constraints at the same time.")
p("Tanzania has built the legal and institutional framework for M&E, yet implementation " 
  "remains weak. The Local Government (District Authorities) Act No. 7 of 1982 gave " 
  "district councils the mandate to plan, implement, supervise and evaluate local " 
  "projects (United Republic of Tanzania [URT], 1982), and the National Policy on " 
  "Decentralisation by Devolution of 2000 transferred resources and decision making to " 
  "those councils under the oversight of the President's Office – Regional " 
  "Administration and Local Government (PO-RALG) (URT, 2000). Mwaijande et al. (2026) " 
  "confirmed that Tanzania has established a Directorate of Performance Monitoring and " 
  "Evaluation in the Prime Minister's Office and M&E units in ministries and local " 
  "government authorities (LGAs), but that institutionalisation remains constrained by " 
  "limited evaluation capacity, weak demand for evidence and the absence of a national " 
  "evaluation policy. Rugeiyamu (2024) attributed the limited contribution of LGAs to " 
  "Development Vision 2025 to dependence on central government, weak financial " 
  "management capacity and inadequate human resources, and reported that ten LGAs held " 
  "completed but non-operational projects worth TZS 3.31 billion in 2021/22 while 87 " 
  "LGAs delayed project completion. Audit reports tabled in April 2026 showed that only " 
  "36.7 per cent of the 38,181 recommendations issued in previous years had been " 
  "implemented and that LGAs continued to record delayed projects and weak contract " 
  "management (Office of the Controller and Auditor General [CAG], 2026). Tanzania " 
  "therefore has a system which exists on paper but which does not consistently correct " 
  "project performance.")
p("Lushoto District Council presents this national pattern at the local level. The " 
  "council covers 3,297 square kilometres in the Usambara Mountains and served 350,958 " 
  "residents in the 2022 Population and Housing Census (National Bureau of Statistics " 
  "[NBS], 2022). The 2012 census recorded 332,436 people, of whom 153,847 (46.3 per " 
  "cent) were men and 178,589 (53.7 per cent) were women, in 71,009 households, 71.4 " 
  "per cent of which were rural (Lushoto District Council, 2015). Its District " 
  "Strategic Plan for 2015/16 to 2019/20 prioritised health, water, education and roads " 
  "and set a target of raising management and governance systems from 55 to 60 per cent " 
  "(Lushoto District Council, 2015). The council finances its water schemes, " 
  "classrooms, health facilities, roads and markets through earmarked central grants, " 
  "sector funds and own-source revenue. Women and children therefore bear the greatest " 
  "cost when a project stalls or when a completed facility remains unused, and no " 
  "systematic study has yet measured the influence of M&E practices on the performance " 
  "of these projects in Lushoto District.")

h2("1.2 Statement of the Problem")
p("A district council should deliver its projects on schedule, within budget and to the " 
  "required technical standards, and the completed facilities should serve the intended " 
  "beneficiaries for their designed life. This outcome requires a functioning M&E " 
  "system. The council should prepare an M&E plan which states baselines, indicators, " 
  "targets, responsibilities and budgets; it should employ qualified and trained M&E " 
  "staff; and it should involve councillors, ward and village authorities, contractors " 
  "and beneficiaries in monitoring and in the use of findings (Kusek & Rist, 2004; URT, " 
  "2000). Herman (2023) confirmed this expectation in Dodoma City Council, where M&E " 
  "planning significantly affected the performance of water supply projects.")
p("The reality in Tanzanian councils falls short of this standard. Kwareh et al. (2024) " 
  "reported that a health project in Dodoma and Dar es Salaam used standard M&E tools " 
  "(84.5 per cent), reporting (73.2 per cent), site visits (67.6 per cent) and " 
  "supportive supervision (57.7 per cent), while participatory monitoring reached only " 
  "39.4 per cent. Killo (2022) identified M&E human resource capacity and technical " 
  "expertise as the strongest influences on project performance in Katavi Region. In " 
  "Lushoto District Council the M&E function operates through the planning structure, " 
  "sector departments supervise their own projects, and community participation remains " 
  "largely confined to project identification. Council reports and audit findings " 
  "record delayed works, cost overruns and under-used facilities, yet no study has " 
  "quantified the extent to which M&E planning practices, M&E human resource capacity " 
  "and stakeholder involvement in M&E explain the performance of local government " 
  "projects in this council.")
p("If this situation persists, the council will continue to commit public resources to " 
  "projects which are delivered late, which cost more than planned and which fail to " 
  "serve the population that requested them. Rugeiyamu (2024) warned that such " 
  "weaknesses limit the contribution of LGAs to national development goals, and the CAG " 
  "(2026) reported that unimplemented audit recommendations persist for years. The " 
  "consequences will fall most heavily on rural women and children, who depend on water " 
  "points, health facilities and classrooms, and they will weaken public confidence in " 
  "devolved government. The study will therefore assess the impact of the M&E system on " 
  "the performance of local government projects in Lushoto District Council.")

h2("1.3 Justification of the Study")
p("The study will benefit several groups, and it will contribute to knowledge. The " 
  "Council Director, the planning and M&E unit, the sector departments and the internal " 
  "audit unit will receive evidence on the M&E dimensions which most affect project " 
  "performance, and they will use it to answer audit recommendations and to improve " 
  "supervision. PO-RALG and the Tanga Regional Secretariat will obtain council-level " 
  "evidence for the targeting of capacity building and oversight to rural councils, and " 
  "the Local Government Training Institute will gain material for M&E short courses " 
  "(Mwaijande et al., 2026). Citizens, ward and village authorities and project " 
  "committees will benefit from greater transparency, ownership and value for money. " 
  "Academically, the study will fill a contextual gap, because most Tanzanian evidence " 
  "comes from cities, from single sectors or from non-governmental organisations rather " 
  "than from a rural mountain district council, and it will add to the African " 
  "literature on M&E institutionalisation.")

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
p("The study will answer three research questions, and it will test three pairs of " 
  "hypotheses on the quantitative strand. RQ1: to what extent do M&E planning practices " 
  "influence the performance of local government projects in Lushoto District? RQ2: how " 
  "does M&E human resource capacity influence the performance of these projects? RQ3: " 
  "to what extent does stakeholder involvement in M&E influence the performance of " 
  "these projects?")
p("H01: M&E planning practices have no significant influence on the performance of " 
  "local government projects in Lushoto District, against H11: they have a significant " 
  "positive influence. H02: M&E human resource capacity has no significant influence on " 
  "that performance, against H12: it has a significant positive influence. H03: " 
  "stakeholder involvement in M&E has no significant influence on that performance, " 
  "against H13: it has a significant positive influence.")

h2("1.6 Scope and Limitations of the Study")
p("In content the study will confine itself to the three specific objectives, and it " 
  "will measure project performance through timeliness, cost efficiency, technical " 
  "quality, utilisation and sustainability, and beneficiary satisfaction. " 
  "Geographically it will cover Lushoto District Council in eight purposively selected " 
  "wards. Substantively it will cover water, education, health, road and market " 
  "projects which the council implemented in the five financial years from 2021/22 to " 
  "2025/26.")
p("The study anticipates four limitations, and it will curb each of them. Staff and " 
  "contractors may withhold information on delayed or defective projects, and the " 
  "researcher will curb this reluctance through guaranteed anonymity and an " 
  "introduction letter. Respondents may recall older projects inaccurately, and the " 
  "researcher will verify their responses against project files and site observation. " 
  "The terrain may slow fieldwork, and the researcher will collect data in the dry " 
  "months and cluster the wards. Some respondents may fail to answer, and the " 
  "researcher will keep a replacement reserve of ten per cent from the same strata.")

h2("1.7 Conceptual Framework")
p("The framework below derives from the problem analysis and rests on results-based " 
  "management (Kusek & Rist, 2004), agency theory (Eisenhardt, 1989) and stakeholder " 
  "theory (Freeman, 1984). M&E planning practices will supply the indicators, baselines " 
  "and targets against which the council measures progress. M&E human resource capacity " 
  "will determine whether the council executes the planned monitoring competently. " 
  "Stakeholder involvement will improve the accuracy, the legitimacy and the use of M&E " 
  "information. The three dimensions will therefore explain variation in project " 
  "performance, subject to the intervening conditions which Figure 1 shows.")

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
p("The researcher will obtain a letter of introduction from the Institute and will " 
  "secure research permission from PO-RALG, the Tanga Regional Commissioner, the " 
  "Lushoto District Commissioner and the Council Director before fieldwork begins. " 
  "Participation will be voluntary and will rest on informed consent. The researcher " 
  "will guarantee anonymity and confidentiality by omitting names, by coding responses " 
  "and by restricting access to the data. No fabricated or plagiarised material will be " 
  "presented, and the researcher will report the findings back to the council.")

h1("CHAPTER TWO: REVIEW OF RELATED LITERATURE")

h2("2.1 Introduction")
p("This chapter reviews the theoretical literature, the empirical literature and the " 
  "relevant policies, and it ends with the gaps which the study will address.")

h2("2.2 Theoretical Literature")
h3("2.2.1 Key Concepts")
p("Monitoring is the continuous collection of data on specified indicators to show " 
  "progress and the use of funds, and evaluation is the systematic assessment of a " 
  "project against relevance, efficiency, effectiveness, impact and sustainability " 
  "(OECD, 2010). An M&E system combines the indicators, the methods, the institutions " 
  "and the processes through which an organisation tracks implementation and assesses " 
  "results (Kusek & Rist, 2004). M&E planning practices are the front-end design of " 
  "that function, comprising the plan, the baselines, the indicators, the targets, the " 
  "tools and the budget (Herman, 2023). M&E human resource capacity is the number, the " 
  "qualifications, the training and the analytical skill of M&E staff (Masvaure & Fish, " 
  "2022). Stakeholder involvement in M&E is the participation of beneficiaries, elected " 
  "leaders, contractors and oversight bodies in data collection, joint site visits and " 
  "corrective decisions (Mgoba & Kabote, 2020). Project performance is accomplishment " 
  "against schedule, cost and quality, together with stakeholder satisfaction and " 
  "sustainability (Ika, 2009). Local government projects are the investments which a " 
  "council plans, finances, procures and supervises under the Local Government " 
  "(District Authorities) Act No. 7 of 1982 (URT, 1982).")
h3("2.2.2 Theories Guiding the Study")
p("Results-based management shifts attention from inputs to outputs, outcomes and " 
  "impact, and it treats the M&E plan, the indicators and the use of information as the " 
  "engine of that shift (Kusek & Rist, 2004). It underpins the first objective. Agency " 
  "theory explains why planning alone is insufficient: each agent from citizens through " 
  "the council to contractors holds more information than the principal holds and may " 
  "pursue its own interest, so monitoring reduces information asymmetry and agency " 
  "costs, and the competence of the monitor determines how well it works (Eisenhardt, " 
  "1989). It anchors the second objective. Stakeholder theory holds that an " 
  "organisation must manage the interests of all groups which affect or are affected by " 
  "its activities, and that their involvement improves the legitimacy and the use of " 
  "information (Freeman, 1984). It anchors the third objective, because beneficiaries' " 
  "participation yields information which outsiders cannot obtain (Mgoba & Kabote, " 
  "2020). The study will be anchored on agency theory and stakeholder theory, " 
  "complemented by results-based management.")

h2("2.3 Empirical Literature")
p("On M&E planning, Herman (2023) used a mixed-methods design with 170 respondents and " 
  "found that M&E planning significantly affected the performance of water supply " 
  "projects in Dodoma City Council. Kwareh et al. (2024) examined a health project in " 
  "Dodoma and Dar es Salaam with 71 respondents and reported strong use of standard M&E " 
  "tools and reporting but weak participatory monitoring. Mabizela and Zwane (2023) " 
  "established that the absence of a functional M&E system contributed to weak service " 
  "delivery in three South African municipalities. These studies treat planning as one " 
  "composite measure.")
p("On M&E human resource capacity, Killo (2022) identified M&E human resource capacity " 
  "and technical expertise among the strongest influences on project performance in " 
  "Katavi Region. Masvaure and Fish (2022) found that capacity strengthening in eight " 
  "African programmes remained ad hoc and focused on individual skills rather than on " 
  "organisational systems. Capacity is therefore often proxied by workshop attendance " 
  "rather than by competence in indicator design and analysis.")
p("On stakeholder involvement, Mgoba and Kabote (2020) demonstrated that participatory " 
  "M&E improved the achievement of community-based water projects in Tanzania, and " 
  "Katerengabo et al. (2023) found that households' involvement in implementing the M&E " 
  "plan significantly influenced the performance of the Tanzania Conditional Cash " 
  "Transfer project (t = 8.472, p < 0.001). Ochen-Ochen (2025) observed, however, that " 
  "political leaders join monitoring for political capital and that M&E evidence serves " 
  "donors more than local users.")
p("Four gaps emerge. Contextually, no published study examines the impact of the M&E " 
  "system on the performance of local government projects in Lushoto District or in any " 
  "council of Tanga Region. Conceptually, scholars treat M&E as one composite variable " 
  "and leave the separate contributions of planning, human resource capacity and " 
  "stakeholder involvement unquantified. Methodologically, most studies rely on a " 
  "single method and cannot verify perceptions against project records or physical " 
  "works. In policy terms, little is known about the way councils translate audit " 
  "recommendations into corrective action. The study will close these gaps by " 
  "disaggregating the M&E system into three measurable dimensions, by measuring " 
  "performance on five verifiable indicators, and by combining regression with " 
  "qualitative enquiry.")

h2("2.4 Policy Review")
p("The National Policy on Decentralisation by Devolution requires councils to plan, to " 
  "implement and to account for local development, and it assigns oversight to PO-RALG " 
  "(URT, 2000). The Local Government (District Authorities) Act No. 7 of 1982 confers " 
  "the council's mandate over local services and projects (URT, 1982). The Third Five " 
  "Year Development Plan for 2021/22 to 2025/26 commits the government to stronger " 
  "implementation, monitoring and evaluation (URT, 2021), and the audit reports tabled " 
  "in April 2026 recommend stronger management of public projects so that they are " 
  "delivered on time and within controlled costs (CAG, 2026). Mwaijande et al. (2026) " 
  "reported that Tanzania still lacks a national evaluation policy. At the local level, " 
  "the Lushoto District Strategic Plan for 2015/16 to 2019/20 contains a monitoring and " 
  "assessment component and sets targets for management and governance systems, so it " 
  "provides the policy basis against which the study will examine M&E arrangements and " 
  "project performance (Lushoto District Council, 2015).")

h1("CHAPTER THREE: METHODOLOGY")

h2("3.1 Introduction")
p("This chapter describes the research design, the study area, the population, the " 
  "sample, the sampling procedure, the data collection methods, the data analysis and " 
  "the ethical considerations.")

h2("3.2 Research Design")
p("The study will adopt an explanatory sequential mixed-methods design embedded in a " 
  "cross-sectional survey and in a single case study of Lushoto District Council. The " 
  "quantitative strand will run first through a survey of M&E stakeholders, and the " 
  "qualitative strand will follow through key informant interviews, focus group " 
  "discussions, document review and site observation to explain the results. Mixed " 
  "methods suit this study because M&E performance questions involve both measurable " 
  "relationships and context-specific explanations, and because the combination of " 
  "survey data with documentary evidence increases validity in development settings " 
  "(Creswell, 2014).")

h2("3.3 Study Area")
p("The study will be conducted in Lushoto District Council of Tanga Region. The " 
  "district lies in the Usambara Mountains, covers 3,297 square kilometres and has " 
  "Lushoto town as its headquarters. It served 350,958 residents in 2022 (NBS, 2022). " 
  "The economy rests on smallholder horticulture, dairy, forestry and tourism, and the " 
  "council implements a large portfolio of water, classroom, health facility, road and " 
  "market projects. Lushoto was chosen because it is a typical rural mountain council " 
  "with a diverse project portfolio, because its strategic plan sets explicit " 
  "monitoring and governance targets, and because reported delays make it an " 
  "information-rich case.")

h2("3.4 Study Population")
p("The study population will comprise all persons who plan, execute, supervise, " 
  "finance, benefit from or oversee the M&E of council projects. The target population " 
  "of 1,087 individuals was derived from council establishment records, from ward and " 
  "village committee registers and from the register of contractors.")

h2("3.5 Sample Size")
p("Sample size will follow the Yamane formula, n = N/(1 + Ne²), where N is the target " 
  "population and e is the precision level of 0.05 at 95 per cent confidence (Yamane, " 
  "1967). With N = 1,087, n = 1,087/(1 + 1,087 × 0.0025) = 293 respondents. The formula " 
  "suits a finite population of known size. A reserve of ten per cent, that is 29 " 
  "respondents, will replace non-responses. In addition, 12 key informants will be " 
  "interviewed, four focus group discussions of eight to ten participants each will be " 
  "held, and 12 project sites will be observed. Table 1 shows the population and the " 
  "proportional allocation of the sample.")

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
p("A multistage sampling procedure will guide the selection of respondents and of " 
  "sites. First, the researcher will select eight wards purposively on the basis of " 
  "project portfolio size, of the presence of completed and of ongoing or stalled " 
  "projects, and of geographic spread across the lowland and the mountain zones. " 
  "Second, the researcher will stratify respondents by the categories in Table 1 and " 
  "will allocate the sample proportionally. Third, the researcher will draw individuals " 
  "from the council staff list, from ward and village committee registers and from the " 
  "contractors' register by simple random sampling with computer-generated numbers. " 
  "Fourth, the researcher will select key informants purposively, namely the Council " 
  "Director, the planning and M&E officer, four departmental heads, the internal " 
  "auditor, two contractors and a development partner representative. Project sites " 
  "will be selected purposively to cover the five sub-sectors and the three " 
  "implementation statuses.")

h2("3.7 Methods of Data Collection")
p("Both primary and secondary data will be collected. A structured questionnaire with " 
  "closed-ended items on a five-point Likert scale will collect primary quantitative " 
  "data on the three M&E dimensions and on project performance. The questionnaire suits " 
  "this study because it reaches a large and dispersed sample at low cost and yields " 
  "standardised data for regression. Semi-structured interview guides and focus group " 
  "discussion guides for ward and village project committees and beneficiaries will " 
  "collect primary qualitative data, and they will allow the researcher to probe the " 
  "reasons for delay and the use of M&E information. An observation checklist will " 
  "verify physical progress, workmanship and utilisation at the 12 sites, and a " 
  "document review checklist will cover the District Strategic Plan, implementation " 
  "reports, project M&E plans and files, payment records and audit reports. " 
  "Triangulation across these sources will strengthen validity (Creswell, 2014).")
p("The researcher will pilot test the instruments with 30 respondents in a comparable " 
  "council outside the sample, and the supervisor with two M&E practitioners will " 
  "review them against the objectives to secure content validity; Cronbach's alpha of " 
  "0.70 or above will indicate acceptable reliability.")

h2("3.8 Data Analysis")
p("Quantitative data will be cleaned, coded and entered into the Statistical Package " 
  "for the Social Sciences (SPSS) Version 27. Descriptive statistics, namely " 
  "frequencies, percentages, means and standard deviations, will summarise respondent " 
  "profiles and the level of each variable. Inferential analysis will use Pearson " 
  "correlation for bivariate relationships and multiple linear regression to test the " 
  "influence of the three M&E dimensions on project performance through the model PP = " 
  "β₀ + β₁MPP + β₂MHC + β₃SI + ε, where PP is project performance, MPP is M&E planning " 
  "practices, MHC is M&E human resource capacity, SI is stakeholder involvement in M&E, " 
  "β₁ to β₃ are the coefficients and ε is the error term. Composite scores will be " 
  "generated from the Likert items of each construct; the assumptions of normality, of " 
  "multicollinearity with a variance inflation factor below 10 and of homoscedasticity " 
  "will be tested; and the hypotheses will be tested at a five per cent significance " 
  "level. Qualitative data will be transcribed, coded and analysed thematically against " 
  "the specific objectives, and the two strands will be integrated through " 
  "triangulation.")

h2("3.9 Ethical Considerations")
p("The study will comply with the requirements which section 1.8 sets out. The " 
  "researcher will obtain an introduction letter and research permission before data " 
  "collection and will seek informed consent from every respondent. Coding of " 
  "questionnaires will protect anonymity, and reporting in aggregate form will maintain " 
  "confidentiality so that no individual or contract can be identified. The researcher " 
  "will avoid fabrication, falsification and plagiarism.")

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
 "Ba, A. (2021). How to measure monitoring and evaluation system effectiveness? " 
 "*African Evaluation Journal, 9*(1), a553. https://doi.org/10.4102/aej.v9i1.553",

 "Creswell, J. W. (2014). *Research design: Qualitative, quantitative, and mixed " 
 "methods approaches* (4th ed.). Sage Publications.",

 "Eisenhardt, K. M. (1989). Agency theory: An assessment and review. *Academy of " 
 "Management Review, 14*(1), 57–74.",

 "Freeman, R. E. (1984). *Strategic management: A stakeholder approach*. Pitman.",

 "Herman, A. K. (2023). Factors influencing monitoring and evaluation planning on the " 
 "performance of water supply projects in Dodoma City Council. *African Journal of " 
 "Emerging Issues, 5*(17), 104–121.",

 "Ika, L. A. (2009). Project success as a topic in project management journals. " 
 "*Project Management Journal, 40*(4), 6–19.",

 "Kacou, K. P., Ika, L. A., & Munro, L. T. (2022). Fifty years of capacity building: " 
 "Taking stock and moving research forward. *Public Administration and Development, " 
 "42*(4), 215–232. https://doi.org/10.1002/pad.1993",

 "Katerengabo, B., Gakuu, C., & Kidombo, H. (2023). Implementing project monitoring " 
 "and evaluation plan with beneficiaries for improving performance: Evidence from " 
 "Tanzania Conditional Cash Transfer. *International Journal of Sustainable " 
 "Development Research, 9*(1), 11–17. https://doi.org/10.11648/j.ijsdr.20230901.12",

 "Killo, P. N. (2022). *Influence of monitoring and evaluation practices on " 
 "performance of tobacco contract farming projects in Katavi Region, Tanzania* " 
 "[Doctoral dissertation, The Open University of Tanzania].",

 "Kusek, J. Z., & Rist, R. C. (2004). *Ten steps to a results-based monitoring and " 
 "evaluation system: A handbook for development practitioners*. World Bank.",

 "Kwareh, K. R., Mgale, Y. J., & Rwela, T. G. (2024). Influence of monitoring and " 
 "evaluation practices on performance of health projects: Evidence from SIKIKA project " 
 "in Dodoma and Dar es Salaam, Tanzania. *Open Access Library Journal, 11*(6), e11470. " 
 "https://doi.org/10.4236/oalib.1111470",

 "Lushoto District Council. (2015). *District strategic plan 2015/16–2019/20*.",

 "Mabizela, H., & Zwane, Z. (2023). Monitoring and evaluation as critical approach to " 
 "enhance the performance of local government: South Africa. *International Journal of " 
 "Research in Business and Social Science, 12*(7), 74–84. " 
 "https://doi.org/10.20525/ijrbs.v12i7.2746",

 "Masvaure, S., & Fish, T. E. (2022). Strengthening and measuring monitoring and " 
 "evaluation capacity in selected African programmes. *African Evaluation Journal, " 
 "10*(1), a635. https://doi.org/10.4102/aej.v10i1.635",

 "Mgoba, S. A., & Kabote, S. J. (2020). Effectiveness of participatory monitoring and " 
 "evaluation on achievement of community-based water projects in Tanzania. *Applied " 
 "Water Science, 10*, Article 200.",

 "Mwaijande, F., Kengera, Z., & Nguliki, I. M. (2026). Evaluation in Tanzania. In R. " 
 "Stockmann, W. Meyer, & T. Stockmann (Eds.), *The institutionalisation of evaluation " 
 "in Africa* (pp. 255–285). Palgrave Macmillan. " 
 "https://doi.org/10.1007/978-3-032-06301-4_10",

 "National Bureau of Statistics. (2022). *The 2022 population and housing census: " 
 "Administrative units population distribution report*.",

 "Ochen-Ochen, I. (2025). The politics of monitoring and evaluation: Implications for " 
 "evidence generation and use. *African Evaluation Journal, 13*(1), a792. " 
 "https://doi.org/10.4102/aej.v13i1.792",

 "Office of the Controller and Auditor General. (2026). *Media statement on the annual " 
 "general reports of the Controller and Auditor General, 14 April 2026*. National " 
 "Audit Office of Tanzania. " 
 "https://www.nao.go.tz/uploads/Media_Statement_-_English.pdf",

 "Organisation for Economic Co-operation and Development. (2010). *Glossary of key " 
 "terms in evaluation and results based management* (2nd ed.). OECD Publishing.",

 "Rugeiyamu, R. (2024). Implementation of Tanzania’s Development Vision 2025: Local " 
 "government authorities’ endeavours and challenges. *Commonwealth Journal of Local " 
 "Governance, 29*, 113–129. https://doi.org/10.5130/cjlg.vi29.8443",

 "United Republic of Tanzania. (1982). *The Local Government (District Authorities) " 
 "Act No. 7 of 1982*. Government Printer.",

 "United Republic of Tanzania. (2000). *National policy on decentralisation by " 
 "devolution*. President’s Office – Regional Administration and Local Government.",

 "United Republic of Tanzania. (2021). *National Five Year Development Plan FYDP III " 
 "2021/22–2025/26: Realising competitiveness and industrialisation for human " 
 "development*. Ministry of Finance and Planning.",

 "Yamane, T. (1967). *Statistics: An introductory analysis* (2nd ed.). Harper and Row.",

]
for r in REFERENCES:
    ref(r)
