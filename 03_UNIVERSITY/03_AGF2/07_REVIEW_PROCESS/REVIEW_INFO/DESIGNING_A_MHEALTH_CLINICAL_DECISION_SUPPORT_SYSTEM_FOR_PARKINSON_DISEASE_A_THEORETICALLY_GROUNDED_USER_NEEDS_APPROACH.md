Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34
https://doi.org/10.1186/s12911-020-1027-1

## RESEARCH ARTICLE Open Access

# Designing a mHealth clinical decision support system for Parkinson’s disease: a theoretically grounded user needs approach


L. Timotijevic [1*], C. E. Hodgkins [1], A. Banks [1], P. Rusconi [1], B. Egan [1], M. Peacock [1], E. Seiss [2], M. M. L. Touray [1], H. Gage [1],
C. Pellicano [3], G. Spalletta [3], F. Assogna [3], M. Giglio [4], A. Marcante [4], G. Gentile [4], I. Cikajlo [5], D. Gatsios [6],
S. Konitsiotis [7] and D. Fotiadis [6]


Abstract


Background: Despite the established evidence and theoretical advances explaining human judgments under
uncertainty, developments of mobile health (mHealth) Clinical Decision Support Systems (CDSS) have not explicitly
applied the psychology of decision making to the study of user needs. We report on a user needs approach to
develop a prototype of a mHealth CDSS for Parkinson’s disease (PD), which is theoretically grounded in the
psychological literature about expert decision making and judgement under uncertainty.


Methods: A suite of user needs studies was conducted in 4 European countries (Greece, Italy, Slovenia, the UK)
prior to the development of PD_Manager, a mHealth-based CDSS designed for Parkinson’s disease, using wireless
technology. Study 1 undertook Hierarchical Task Analysis (HTA) including elicitation of user needs, cognitive
demands and perceived risks/benefits (ethical considerations) associated with the proposed CDSS, through
structured interviews of prescribing clinicians (N = 47). Study 2 carried out computational modelling of prescribing
clinicians’ (N = 12) decision strategies based on social judgment theory. Study 3 was a vignette study of prescribing
clinicians’ (N = 18) willingness to change treatment based on either self-reported symptoms data, devices-generated
symptoms data or combinations of both.
Results: Study 1 indicated that system development should move away from the traditional silos of ‘motor’ and
‘non-motor’ symptom evaluations and suggest that presenting data on symptoms according to goal-based
domains would be the most beneficial approach, the most important being patients’ overall Quality of Life (QoL).
The computational modelling in Study 2 extrapolated different factor combinations when making judgements
about different questions. Study 3 indicated that the clinicians were equally likely to change the care plan based on
information about the change in the patient’s condition from the patient’s self-report and the wearable devices.

Conclusions: Based on our approach, we could formulate the following principles of mHealth design: 1) enabling
shared decision making between the clinician, patient and the carer; 2) flexibility that accounts for diagnostic and
treatment variation among clinicians; 3) monitoring of information integration from multiple sources. Our approach
highlighted the central importance of the patient-clinician relationship in clinical decision making and the relevance
of theoretical as opposed to algorithm (technology)-based modelling of human judgment.


Keywords: mHealth, M-health, Digital health, Clinical decision support system, CDSS, User needs, Parkinson’s,
Mobile devices, Wearables


[* Correspondence: l.timotijevic@surrey.ac.uk](mailto:l.timotijevic@surrey.ac.uk)
1Faculty of Health and Medical Sciences, University of Surrey, Guildford, UK
Full list of author information is available at the end of the article


© The Author(s). 2020 Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0
[International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and](http://creativecommons.org/licenses/by/4.0/)
reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to
the Creative Commons license, and indicate if changes were made. The Creative Commons Public Domain Dedication waiver
[(http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated.](http://creativecommons.org/publicdomain/zero/1.0/)


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 2 of 21



Summary points


 - There has been limited evidence of the widespread
implementation and acceptance of mHealth based
Clinical Decision Support Systems (CDSS).

 - The needs of the users of mHealth CDSS (i.e.
clinicians) in terms of the cognitive demands of
clinical decision making under uncertainty are not
explicitly explored in the of design mHealth-based
CDSS.

 - Our research on clinicians’ user needs for the
development of Parkinson’s mHealth-based CDSS is
theoretically grounded in the psychological literature
about expert decision making and judgement under
uncertainty.

 - It highlighted the central importance of the patientclinician relationship in clinical decision-making and
the relevance of theoretical as opposed to algorithm
(technology)-based modelling of human judgment.


Background
We are currently witnessing a paradigm shift in the global
provision of healthcare, as new technologies are emerging
to address growing challenges of cost, quality and continuity of healthcare provision. Rapid technological developments such as mobile health technologies (mHealth) and
data analytics, offer solutions to the current unsustainable
healthcare systems. “Mobile health” (mHealth), is defined
as “medical and public health practice supported by mobile devices, such as mobile phones, patient monitoring
devices, personal digital assistants and other wireless devices” [1]. mHealth is incorporated within the broader
health informatics framework, though has emerged as a
distinctive system in terms of context of use and acceptance. The pervasiveness, portability, convenience, immediacy and ubiquity of mobile devises enables not only
continuous monitoring and communication required for
the management of chronic conditions by healthcare providers at lower costs, but also patient empowerment to
self-manage chronic conditions. Furthermore, the unique
feature of mHealth is its ability to collect and connect
medical, health-related and non-medical (e.g., behavioural)
information that can feed into the existing health informatics systems such as electronic medical records and hospital information systems. This potentially innovative
aspect of mHealth solutions, however, is currently largely
confined to the non-healthcare context (e.g. lifestyle and
public health applications) and lacking in acceptable
frameworks for its wider adoption into the healthcare systems [2, 3] . Diffusion of new technologies necessitates
clarifying the actual purpose of the innovations both from
the point of view of healthcare system and the immediate
needs of the users of the system, including patients and
clinicians.



The need for mHealth-based clinical decision-support
system
For a health informatics system to be useful it needs
to address all the complex cognitive needs of a clinician’s task. Medical decision making, especially concerning chronic conditions, is characterised by
considerable complexity as it is often based on uncertain and incomplete information and therefore relies
on the clinician’s expertise. The diversity of patient
presentation and complexity of symptoms, time constraints, characteristics of patient–clinician encounter,
and limitations of diagnostic tests all increase uncertainty in medical decision making, resulting in poor
patient outcomes and increased costs [4–11]. Diagnostic uncertainty is ostensibly a subjective
phenomenon based on the perceived lack of reliable
information for treatment decisions [5].
The advances in mHealth such as data analytics and algorithm development based on continuous capture of a
wide range of structured and unstructured patient-related
data, can be harnessed to address such uncertainties
through a Clinical Decision-Support System (CDSS) [12,
13], a software that can aid clinical decision making
through careful matching of the patient individual factors
(e.g., age, sex, ethnicity, computer literacy), their behaviour
(in-situ and self-reported behaviour) and their current
health status, with a computerised clinical knowledge base
in order to provide patient-specific assessment and recommendations about clinical diagnosis/management [14]. A
mHealth-based CDSS offers the potential to reduce medical errors [15] and improve the quality and efficiency of
healthcare [16]. Nevertheless, actual application of such
systems to date has been limited [17]. Several systematic
reviews have examined the ability of mobile technologybased interventions designed to improve healthcare service
delivery [18, 19]. Free et al. [18] identified a small improvement in outcomes relevant to clinical diagnosis, though the
potential errors in reports and time taken to process data
do caution against a wholesale and uncritical adoption of
mHealth solutions. Bright et al. [20] similarly suggested
that the evidence of their impact on clinical and economic
effectiveness, user satisfaction and usefulness is ambiguous,
with a range of studies variously demonstrating high, low
and no difference in satisfaction and usefulness after introducing such CDSS’s in clinical decision making. The authors conclude that understanding the ways in which
CDSS can meaningfully enhance specific clinical roles is a
necessary next step towards the successful implementation
of mHealth-based CDSS. In developing a mHealth CDSS,
therefore, user-centred design is essential.
In software engineering, user-centred design comprises
several key aspects: a) analysis of users’ characteristics
and work environments; b) top level functional analysis
of users’ goals, the domain structures needed for


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 3 of 21



successful goal completion, and information flows within
a system; c) tasks analysis; and d) representational analysis of user interface [21]. These software engineeringdriven analytical strategies are mostly performed
through ‘use cases’ - the industry standard for establishing system requirements. Whilst a use case approach facilitates requirement- gathering and subsequent
description of the functional requirements of a system
from a goal-based user perspective [22], it centres on the
system architecture and system/service quality rather
than the system user, is iterative and incremental, and
mainly driven by the already established system prototype. By contrast, a fully user-centred approach precedes
the development of the prototype and provides a nuanced understanding of intended users’ needs before the
process of software development even commences.
In this paper, we report on research of user needs to
inform and provide first principles for the development
of the prototype of a mHealth CDSS [23] for a complex
neurodegenerative condition – Parkinson’s disease (PD).
Focusing on this particular chronic condition, our aim is
to present a novel approach to establishing user needs,
utilising a suite of methodologies that can be applied to
a range of disorders. These methodologies are theoretically grounded in the psychological literature about expert decision making and judgement under uncertainty.
Thus, they address the gap in the currently reported user
studies for the development of CDSS which often lack a
theoretical basis for their study design [24]. The unique
characteristics of PD provide a fertile ground for the implementation of a CDSS based on mHealth, but due to
its complexity, also present many challenges.
Parkinson’s was chosen because of its high prevalence in
older adults and its complex and ever fluctuating symptom range. PD is the second most common neurodegenerative disorder in Europe with more than 1 million
people living with the disease in Europe today and this
number is forecast to double by 2030 [25]. The economic
impact of the disease is substantial – the annual European
cost is estimated at €13.9 billion [26]. Parkinson’s is a
complicated disorder that most patients live with for many
years and decades, becoming increasingly reliant on others
to care for them in all aspects of life. The highly idiosyncratic presentation of the disease, its unpredictable progression, the plethora of possible symptoms both motor
(tremor, bradykinesia, rigidity as well as gait/postural balance, speech disorders, swallowing disorders) and nonmotor (cognitive disorders/dementia, depression and anxiety, Impulse Control Disorders, sleep disorders), as well
as their daily and hourly fluctuation (e.g. motor on-off
fluctuations, including freezing and dyskinesia’s, and nonmotor fluctuations) render the disease particularly difficult
to manage. The treatment is typically pharmacological,
supplemented by occasional rehabilitative therapies, and



in some cases, surgery. Clinical decisions are usually based
on routine patient-clinician meetings (every 3–6 months).
In that context, clinician reliance on patient and carers’
self-reports may be problematic. The presenting state of
the patient may not indicate the extent and nature of
functional impairments that are experienced at other
points in time meaning that the clinician cannot gain a full
and accurate picture of the patient’s status and the disease
fluctuations that are crucial for appropriate titration of
pharmacological treatment. Thus, a CDSS delivering a
continuous stream of information via a mHealth solution
has many obvious attractions, due to its pervasiveness,
portability, context-sensitivity, immediacy and convenience [27].


User-centred development of CDSS based on mHealth
A mHealth-based CDSS promises to deliver objective data
about the patient’s healthcare status to the clinician in a
timely manner [1] but, at the same time, risks increasing
“technical uncertainty” [4], that is, the uncertainty due to
the increased amount of available information, but not necessarily its utility, in making medical decisions. In addition,
it has been shown that human beings tend to rely more on
human judgement rather than on evidence-based algorithms, despite the latter being better predictors in many
contexts (a phenomenon called “algorithm aversion” [28]).
An effective CDSS must be able to collect and link
numerous types of patient-related data, be they physiological, pharmacological, behavioural and/or psychological
measures. When developing the CDSS, a decision must be
made about what types of data will be collected, connected and ultimately delivered to the clinician to optimise their judgment. Optimizing medication is the key for
the management of PD and to support such functionality,
the CDSS must employ algorithms that transform the
stream of patient data into recognised symptoms (in order
to recognise a patient’s state), and then to proposed decisions about the treatment plan. To develop accurate decision support systems, merely providing patient data is not
enough; it needs to identify underlying expert models of
decision making and compare the data against these expert models and clinical guidelines [29].
This includes an understanding of how clinicians interpret and respond to uncertain evidence. The latter is
particularly relevant to PD given its multifaceted, complex and fluctuating nature [30–33]. It is important to
understand whether and to what extent clinicians perceive a certain piece of evidence as informative and
whether it is coming from a subjective information
source (e.g., patient self-reports, diaries, questionnaires)
or from an objective source e.g., wearable digital health
technology, neuropsychological assessments, medical assessment techniques (such as Magnetic Resonance Imaging (MRI), blood samples) [34–36].


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 4 of 21



Early user (clinician) engagement with the design
process and well-structured studies of user needs and
their cognitive demands are therefore a necessary component of mHealth-based CDSS design and essential to increasing the usefulness, efficacy and acceptability of
mHealth technologies. However, user engagement in the
development of the CDSS is poorly reported and often
given only a cursory role in the design. There is limited
evidence of extensive exploration of clinicians’ decisionmaking processes, and how interventions will fit into routine clinical workflow. Previous design projects on CDSS
for Parkinson’s, PERFORM [37], REMPARK [38] and
SENSE-PARK [39], surveyed the factors influencing clinicians’ pharmacological decision-making – for instance,
Serrano et al. [24] report on the participatory design
process to achieve a consensus among patients, clinicians
and technologists over the selection of a set of symptom
domains to be continuously assessed. The reviewed projects, however, mainly focused on information needs and
none examined in-depth the clinicians’ expert judgement
models that are active in situ – the contexts characterised
by the specific presentation of symptoms. Importantly,
none of these approaches were grounded in the theoretical
literature around task analysis, cognitive demands, expert
judgments and cognitive processes under the conditions
of the varying degrees of certainty. This limitation was addressed in the studies reported below.


Aims and overall approach
We report on PD_Manager, a case study of clinicians’ user
needs for the development of a mHealth-based CDSS designed to help clinicians to monitor motor and non-motor


Fig. 1 Implementation of the CDSS for the clinician



symptoms using easily portable devices such as smart
phones, wristbands and sensor insoles, worn by patients,
to capture objective data about their fluctuating condition.
The system is intended to combine machine learning and
decision support methods with mobile and cloud-based
approaches and share data via the cloud enabling clinicians to follow patients’ status closely. In this way, the
PD_Manager CDSS enables continuous and accurate patient monitoring and PD symptoms assessment, delivered
in a timely manner (see Fig. 1).
The aim of the mHealth-based CDSS is to enable the
monitoring of patients, fluctuation of a range of symptoms or medication/treatment adherence, so that management plans can be evaluated and indications for
modifications to medication regimens identified. The
models for PD_Manager CDSS were developed through
a combination of data mining of various PD symptoms;
expert modelling using a qualitative multi-criteria
method DEX, and assessment of models in terms of classification accuracy, transparency, correctness and completeness. This methodology is reported in a separate
publication [40].
Due to the nature of the decision making (i.e. medication changes in a progressive chronic disease), which
rarely if ever regards life threatening or emergency
events, Quality of Services (QoS) aspects such as latency,
priority and bandwidth were not critical for the development of the CDSS. Data loss was minimized as much as
possible given that the system adopted commercial sensors. Other QoS aspects, such as power consumption
were very important for the patient experience with the
system and were taken into consideration both for the


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 5 of 21



design of the system and for the pilot implementation.
Data security was also addressed in the design and implementation of the mHealth system and was the main
requirement for QoS within the PD_manager context.
In order to develop an initial set of principles for
the CDSS, a series of user-needs studies were initially
conducted, which we are reporting in this paper. The
overall objective of our user-centred approach was to
identify:


I. What types of decisions clinicians make when
managing a patient with PD?
II. Information needs of the clinicians: What factors
and their combination related to the patient
symptoms inform their decisions?
III. Judgement under conditions of varying degree of
certainty: What is the perceived value of selfreported patient data vs mHealth-generated data for
a range of clinical decisions?


The following suite of three studies were conducted:


Study 1 - Hierarchical Task Analysis (HTA) including
elicitation of user needs, cognitive demands and
perceived risks/benefits (ethical considerations)
associated with the proposed CDSS.
Study 2 - Computational modelling of clinicians’
decision strategies.
Study 3 - Vignette-based study of the relative value of
self-reported vs CDSS-generated evidence for clinicians’
decision making.


Study 1 utilised HTA through structured qualitative interviews, [41] as the framework for examining tasks associated with the clinical management of PD in terms of goals
and sub-goals as well as the ethical considerations likely to
arise when clinicians use mHealth-based CDSS. HTA, a
core ergonomics methodology, is the established precursor
for exploration of cognitive demands associated with human performance across a wide variety of domains and
applications.
Study 2 is grounded in social judgement theory and related methodology [42]. This method has been used in
many areas, and there has been extensive research on
clinical judgement using it in a number of medical domains including studies of chronic heart failure [43], the
management of rheumatoid arthritis [44], and decisions
to use dialysis [45]. This approach aims to describe judgments through the combination of cues, such as signs or
symptoms that are used to diagnose a cause or predict
an outcome. Previous research on Parkinson’s disease
has identified a comprehensive set of symptoms of relevance to managing the disease [24, 46]. Whilst this objective set of symptoms provides a useful framework of



possibilities, which of these symptoms users actually use
in their judgement process is a different question. A
common finding across all domains of professional judgments, including medical judgments, is that the cues
people actually use in their decisions are not the same as
the cues they explicitly report using [47]. Experts use
less information when making decisions than novices

[48] and often disagree about their judgments [48]. Fully
understanding user needs therefore requires an approach
that captures the variation, context, and subjective
weighting of each piece of information for individual
users.
Study 3 builds on this recognition of the need to contextualise experts’ medical decision making by further exploring the situated nature of these judgements. It recognises
the importance of understanding whether and to what extent clinicians perceive a certain piece of evidence as informative as a function of whether it comes from a
subjective (e.g., patients’ self-reports, diaries) or from an objective (e.g., wearable technology, electrophysiological and
neuroimaging techniques) source [35, 36]. In addition, we
explore the uncertainty inherent in evaluating these types
of evidence in situ by varying the degree to which the evidence from the two sources are congruent with each other.
We deploy vignettes, a methodology that has already been
successfully used to study how novices and experts make
judgements in conditions of uncertainty based on patients’
self-reports as well as objective evidence, such as a physical
symptom [49–51].
The data were collected between 2015 and 2017. Since the
three studies collected data from clinicians (not patients), a
formal ethical approval was not required within any of the
national legislations (UK, Greece, Slovenia and Italy). However, within the UK, Research & Development approval from
the hospital trusts - the two hospitals that allowed access to
the clinicians - was obtained. For each study, written Informed Consent was obtained from the participants.


Method
Study 1: Hierarchical Task Analysis
Data were collected across four culturally diverse sites (UK,
Italy, Slovenia and Greece) and from two core user groups:
Prescribing clinicians (consultant neurologists, hospital doctors, general practitioners (GPs) and Parkinson’s disease
nurse specialists (PDNS) and supporting clinicians (physiotherapists, occupational therapists, psychologists, speech
therapists). A mixed-method approach was used whereby
Prescribing Clinicians were interviewed one-to-one and
Supporting Clinicians were either interviewed one-to-one or
took part in a small focus group. The Prescribing and Supporting Clinicians recruited for the study are detailed by
country (Table 1).
The added value of our cross-cultural approach is the
ability to account for diverse models of clinical work


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 6 of 21


Table 1 Participant description


UK Italy Greece Slovenia Total
n = 6 n = 15 n = 8 n = 18 N = 47


Prescribing clinicians


Consultant neurologist 2 4 8 7 21


Parkinson’s disease nurse specialist 3  -  -  - 3


General practitioner 1 5  - 3 9


Supporting clinicians


Physiotherapist  - 2  - 2 4


Occupational therapist  - 1  - 2 3


Psychologist  - 3  - 2 5


Speech therapist  -  -  - 2 2



organisation. Whilst working in multi-disciplinary teams
for complex neurological diseases such as PD is standard
practice in state medical systems such as UK, Italy and
Slovenia, the Greek system is characterised by a predominant role of consultant neurologists within the state system, supplemented by specialist treatment in the private
system.
The first step was to clearly define the overall task
under analysis and the specific purpose for that analysis.
Within this study the top-level task and goal were collectively defined as:


‘Effective management of Parkinson’s disease in
order to identify where the proposed outputs of the
PD_manager project can add value to the task’.


There followed a desk-based review of current practice
from the literature resulting in the development of a
preliminary Hierarchical Task Diagram (HTD). Utilising
this preliminary HTD as a stimulus, data were collected
from the prescribing and supporting clinicians via structured qualitative interviews (locally, within each of the 4
countries) to expand our understanding of the task, to
determine task sub-goals and ultimately to achieve full
task decomposition. During the interviews clinicians
were asked to reflect on the preliminary HTD and suggest any changes/amendments to accurately reflect the
broadest range of tasks they typically undertake. Cognitive demands, decision-making strategies, perceived usefulness of symptomatic data, perceived importance of
patient adherence, supporting therapies and beliefs
about mHealth-based CDSS (including ethical considerations) were elicited in parallel by a generalist approach
within the interview to allow us to encompass the whole
domain more effectively.


Study 2: Modelling clinicians’ decision strategies
The aim of this study was to develop a model of how clinicians use information from patients with Parkinson’s



disease in the management of PD using a factorial survey
design. We elicited the decision-making strategies of clinicians, describing how strongly weighted each of the factors
are within their overall judgements. Prescribing clinicians
assessed 24 cases, each one describing the symptoms of a
different patient. For each case, clinicians were asked to
make judgements about the patient. Specifically, they
made judgements about changing the care plan, change to
Levodopa, and change to dopamine agonist. In each case,
13 key symptoms or factors in the assessment of Parkinson’s disease were varied systematically. These were: bradykinesia, rigidity (stiffness), tremor, gait and balance,
sleep, cognitive functioning, depression, constipation,
motor fluctuations, dyskinesia, impulsivity, age and employment status. The changes in these symptoms were described to clinicians in terms of a comparison to a
consultation three to 4 months previously. That is, each of
the symptoms was described as ‘better’, ‘same’, or ‘worse’
than three to 4 months previously. Two contextual factors
were: age (either ‘55 years old’ or ‘75 years old’) and employment status (either ‘employed’ or ‘retired’). Participants were informed that in all cases they should assume
that the patient with Parkinson’s disease was currently
taking Levodopa and a dopamine agonist, the disease duration is 5–10 years and their disease severity is stage 3 on
the Hoehn and Yahr scale [52] (please see the Table 2 for
an example of a case).


Study 3: vignette study of value of different types of
information for clinicians’ diagnostic strategies
The study aim was to investigate clinicians’ decision making about treatment and care plans based on the relative
utility of subjective (reported by a patient with Parkinson’s
disease) or objective (digital health) information. Prescribing clinicians completed an online questionnaire with 15
vignettes describing situations involving hypothetical patients with Parkinson’s disease (the surnames used in the
vignettes were not of real patients). For all vignettes, the
main information about the patients was kept constant:


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 7 of 21


Table 2 An example of the Study 2 case


Demographics Motor Symptoms Non-motor symptoms Treatment adverse effects


75 years old, retired Bradykinesia Worse Sleep Better Motor fluctuations Same


Rigidity (stiffness) Worse Cognitive functioning Same Dyskinesia Better


Tremor Worse Depression Same Impulsivity Better


Gait & balance Same Constipation Better



they were described as older (between 66 and 70 years
old), living with their partner, with their symptom severity
at Hoehn and Yahr stage 3, disease onset was 7 years ago,
and the current therapy as prescribed for the past 6
months. Furthermore, we randomly varied the patients’
gender across the 15 vignettes.
Two within-participant variables were manipulated in
these vignettes: information type (5 levels) and symptoms/signs (3 levels). We manipulated the type of information presented to the clinicians as follows (see
Table 3): subjective information (patients’ self-report);
objective information (digital health data); congruent
subjective and objective information (both sources suggested a decline in patients’ symptoms/signs); incongruent subjective and objective information (one indicating
a decline and the other indicating an improvement).
For each information type, we devised three different
scenarios where the main difference was the symptom/
sign: (1) bradykinesia [53, 54], and impaired dexterity, (2)
gait and postural stability, and (3) sleep. The following is a
sample vignette presented to participants depicting a case
of incongruence between the patient’s self-report (indicating a decline in gait and postural stability) and a sensor insole (indicating an improvement):


“Mr Briggs is 69 years old, retired, and he lives with his
wife. He suffered from the first symptoms of PD approximately seven years ago (Hoehn and Yahr stage 3).


In a consultation with you, the patient tells you that
he feels that his condition has worsened and he has
been experiencing more falls and gait difficulties.


Data from the patient’s sensor insole, a device which
has captured information on his PD symptoms, show
that he has improved and has experienced a



decreased number of falls and gait difficulties since
his last clinical consultation.


The patient has been receiving medication and
physiotherapy treatment over the last 6 months.”


After reviewing each vignette, participants were asked to
select a decision about the therapy (“Based on this information, how likely would you change the patient’s care
plan?”) using a 7-point Likert scale (1 = very unlikely, 7 =
very likely), and about the confidence in the decision
(“How confident are you in the answer you have just
given?”, 1 = not at all confident, 7 = very confident). Finally, they were asked to indicate what type of data they
would find more useful in order to increase confidence in
their decision – subjective (PD patient’s self-report) or objective (devices-generated) data (“Given your decision,
how useful would you find it to seek for more information
from the patient or the devices to increase your confidence?”). They used two 7-point Likert scales (1 = not at
all useful, 7 = very useful) to provide their answer for both
the self-report and the device-generated data.
After completing the vignettes, participants’ sociodemographic data (including age, gender, and nationality)
were collected. The survey lasted approximately 30 min.


Results
Study 1: Hierarchical Task Analysis
Analysis of the qualitative data comprised a mixture of
summative content and thematic analysis [55]. Coding
structures were developed to guide the analysis of the
data and ensure a harmonized and standardized approach to analysis of the data across the different countries. The resultant data were used to develop an
updated version of the Hierarchical Task Diagram validated by the interview process (Fig. 2).



Table 3 Information about the manipulated information type variable in Study 3


Variable Levels


Information type Subjective Objective Subjective & objective – Subjective & objective –
(self-report) (device outcome) congruent incongruent
Self-report: decline


Devices: improvement



Subjective & objective
–incongruent
Self-report: improvement


Devices: decline


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 8 of 21


Fig. 2 Hierarchical Task Analysis Diagram reflecting sub-goals and task operations for both Prescribing and Supporting Clinicians



The majority of clinicians interviewed in this study operated in an environment with little or no access to continuous objective data on PD motor symptoms to
support their clinical decision making, even at its most
basic level. Therefore, the provision of this type of data
in graphical form by the mHealth-based CDSS was
deemed to be useful. Having identified the cognitive demands and difficulties clinicians experienced when managing patients and their expressed needs (Appendix 1) as
well as the perceived usefulness of data on the various
motor and non-motor symptoms (Appendix 2), a set of
user-derived requirements for the mHealth-based CDSS
design were proposed (Appendices 3 and 4).
Approaching the development of user needs using this
methodology, the outcomes of this study suggested a move
away from the traditional silos of ‘motor’ and ‘non-motor’
symptom evaluations and suggest that presenting data on
symptoms according to goal-based domains would be the
most beneficial approach. This innovative goal-based domain approach including: Diagnosis indicators; Disease progression indicators; Pharmacological decision support;
Patient safety; Overall QoL indicators; Physiotherapy/Occupational therapy; Psychology and Speech therapy (Appendix
3) would facilitate the collation/integration of the relevant
non-motor symptom data with the motor symptom data for
each of these domains in more targeted and user-friendly interfaces. Furthermore, the data suggested that the most useful symptoms to evaluate should be driven by the
importance the patient themselves attribute in terms of their
overall QoL. Therefore, it was suggested that design should
deliver functionality to allow for the creation of personalised



user interfaces that provide flexibility for clinicians/patients
to identify and select which symptoms they wished to consider at any one time. The availability of such a flexible system should allow clinicians to focus on the data they needed
to engage with, to better facilitate patient engagement in
shared decision making and potentially achieve better adherence and clinical outcomes.
Finally, the content analysis of attitudes towards the technology and ethical issues indicated that the participants were
not aware of any ethical issues associated with the mHealthbased CDSS. There seemed to be a general agreement that
the systems needed to manage privacy concerns were
already in place such as, for instance, data management processes and consent forms. However, when asked whether
they were aware of any governance guidelines /codes of
practice regarding the collection and transmission of patient
data using technology, none of the participants were able to
refer to these systems within the context of their work.


Study 2: Modelling clinicians’ decision strategies
Twelve prescribing clinicians (7 males and 5 females), with a
mean age of 45.58 years, (SD = 8.76) from 4 countries: Italy
(n = 3), Greece (n = 2), Slovenia (n = 3) and the UK (n = 4)
took part in the study. They were consultant neurologists
(n = 9), consultant gerontologist (n = 1) and general practitioners (n = 2). These clinicians saw a mean of 172.67 patients with Parkinson’s disease per year (SD = 215.26).
Multiple regression was used for each clinician to determine
the weighting of each of the factors on each of the judgements. The judgement patterns were calculated for each
participant individually based on their responses to the


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 9 of 21



judgement task. Each of the factors within the cases was
coded as an independent variable and the judgements made
about each case were the dependent variables. The R [2] value
for the regression model describes how well the factors explain the judgements made and the standardised beta
weights for each factor describe the weighting of that factor
in the judgement. Table 4 presents the beta weights for each
factor in each judgement and the R [2] for each model.
Across the different models, findings showed that clinicians were more likely to change the care plan and increase the level of medication when presented with
worsening symptoms, with the exception of a reduction in
Levodopa with worsening dyskinesia and a reduction in
dopamine agonist with worsening impulsivity. Analysing
the findings in more detail provides some more specific
results. Across the different judgements, the factors that
dominate the decision are motor symptoms: bradykinesia;
rigidity; motor fluctuations; and tremor. Non-motor
symptoms such as depression, impulsivity and cognitive
function explained some variance in the judgements, albeit less than bradykinesia, rigidity, motor fluctuations
and tremor, but sleep and constipation had very little effect on the judgements made. Some factors were weighted
more similarly by all clinicians, e.g. tremor, whereas others
were weighted more differently, e.g. bradykinesia. Furthermore, the study shows that different factor combinations
(e.g. symptom, age, employment status) are important
when making judgments about different questions (e.g.
changing the care plan, change to Levodopa, and change
to dopamine agonist).


Table 4 Standardised beta weights for the mean response to
identify the factors predicting changes to treatment


Factor Care Plan Levodopa Dopamine Agonist


Bradykinesia .36 .31 .14


Tremor .51 .47 .44


Gait −.02 .16 −.04


Dyskinesia .19 −.29 .31


Motor Fluctuations .44 .44 −.16


Sleep .10 .04 .19


Cognition .23 .27 .00


Impulsivity −.09 −.07 −.36


Depression .22 .08 .27


Constipation −.02 −.10 .06


Rigidity .35 .41 .34


Age −.31 −.07 .00


Employment −.37 −.29 .26


Model R [2] 0.82 0.90 0.70


N.B. for symptoms, a positive beta weight implies an increased likelihood of
change to the care plan, or an increased level of medication, in response to
worsening symptoms



Study 3: Vignette study of value of different types of
information for clinicians’ diagnostic strategies
Participants were N = 18 (10 females; 8 males) prescribing
clinicians practicing in Greece (8), Italy (5), the UK (4),
and Slovenia (1). Their mean age was 41.94 (SDage = 7).
They were consultant neurologists (13), general practitioners (2), consultant gerontologist (1), neurology resident (1), and researcher (1).
In our analyses, given that our main variable of interest
was Information Type, we averaged participants’ responses
across the three primary symptoms. The results indicated
that the clinicians were equally likely to change the care
plan based on information from the patients’ self-report
and the devices about the decline of their condition. In
addition, they were more likely to revise the care plan
when they received congruent information from both
sources and less likely to revise the care plan when they received conflicting information from both sources (Fig. 3).
The findings about clinicians’ confidence in their decision mirrored these findings. Clinicians were equally
confident in changing the care plan when receiving information from only one information source, most
confident when the information from both sources was
congruent and least confident when it was incongruent.


Discussion
As highlighted by Castro et al. [56] a crucial question to ask
in the development of a CDSS is: What is the system
intended for? Therefore, the early understanding of user
needs is the most important aspect of system development.
And yet, the predominance of the software engineeringdriven CDSS development with a main focus upon information needs of a user and use cases based on the already established prototypes [24], is unlikely to provide a full account
of the social (e.g., the interactions between patients, caregivers, and clinicians; time constraints) and psychological
(e.g., clinicians’ judgement and decision-making strategies)
realities within which the technology will be operationalised.
We addressed these shortcomings in our research.
Our approach to user studies was developed to identify
the core principles of design to guide an early development of the CDSS. Based on our findings, we can formulate three main principles of design with some important
theoretical and practical implications: 1) enabling shared
decision making between the clinician, patient and the
carer; 2) flexibility that accounts for diagnostic and treatment variation among clinicians; 3) monitoring of information integration from multiple sources.


Implications for the system design
Our study highlighted that the primary goal of the system
should be to enable shared decision making between the
clinician (e.g., neurologist, PD nurse, physiotherapist), patient and the carer [57, 58]. This is evident in several


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 10 of 21


Fig. 3 Mean likelihood of changing the patients with Parkinson’s Disease care plan as a function of the different pieces of information presented
to participants in the scenarios (i.e., self-report only, devices’ outcome only, consistent (congruent) or conflicting (incongruent) information from
both sources). Error bars represent 95% confidence intervals



findings: our HTA interview study (Study 1) has highlighted
that the needs of clinicians should be conceptualised in
terms of how the system is likely to support the clinicianpatient interaction. The practical implication of this finding
is that the design should be driven by the patient-specific
goal-based domains rather than the expert-defined symptom
categorisation. Study 1 identified that the most useful symptoms to evaluate should be decided by the importance patients themselves attribute to those symptoms in terms of
their overall QoL. A mHealth-based CDSS should therefore
be conceptualised as a vehicle that facilitates co-production
of disease management solutions and should be embedded
within the context of patient-clinician interaction.
The shared nature of decision making extends the approach to decision making applied in Study 2. Previous
work applying social judgement theory to clinicians’ decision making uses a paradigm in which an individual clinician is presented objective information and forms a
judgement about the patient. From this analysis their personal evaluation can be inferred [43–45]. The context of
this study demonstrates that an individual clinician’s
weighting of cues is not the only consideration. Instead,
the weighting of symptoms and desirability of outcomes
may emerge through the interactions of clinicians, patient,
and carer. Study 3 extends the approach to decision making, demonstrating how the weighting of this information
is also influenced by its source – the patient’s subjective



report or digital device, thus highlighting again the key
role of the clinician-patient interaction and communication. The unique context of mHealth devices, in comparison to digital devices in more established settings such as
hospitals, further influences their interpretation.
Secondly, our suite of studies highlighted that the system should take into account diagnostic variation [5] as
well as treatment variation among clinicians. In other
words, a CDSS should allow different judgement patterns
for the disease management to operate for similarly presented symptoms. The evidence for this principle emerged
from Study 2, which identified similarities in the way clinicians evaluate symptoms, which, nevertheless, may be
linked to significant variations in the way in which the disease is ultimately managed. Whilst the study did not report on the actual causal models underpinning this
variability, it indicated that different users are likely to prefer different information in management of the disease.
This variation is potentially driven by not only symptoms
presentation but also the immediate as well as broader
context of patients’ lives. Again, this illustrates that it is
not possible to define a set of the most important factors
for all cases, but rather, that the system must have an inbuilt flexibility to allow the operation of different solutions
representing co-production by clinician and patient, which
would improve the completeness and usefulness of the
model. This flexibility should be combined with a method


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 11 of 21



to optimize the quality and overall performance of the
decision-making process. The recent developments in
quality of service-based web- service selection [59] may be
one way forward in the identification of the most important factors that address user needs and increase user satisfaction whilst maintaining system flexibility.
Finally, our work pointed to the necessity for a system to
fully account for and continuously monitor the shortcomings, risks and compromises inherent in integrating quantitatively different types of information from multiple sources.
Study 3 provides evidence that the combination of information from the patient and from the mHealth devices can differentially influence experts’ decisions and their confidence
in those decisions. This is demonstrated by the statistically
significant differences between the conditions in which both
types of information were presented (i.e., the congruent and
incongruent conditions) and the conditions in which only
one source of information (either the patients’ self-report or
the devices’ outcomes) was available. The lack of difference,
both in terms of their impact on the care plan revision and
the confidence levels, between the patients’ self-reports and
devices’ outcomes suggests that clinicians consider the - ostensibly subjective - information provided by patients as
equally useful and trustworthy as the objective information
generated by the devices. This finding about the clinicians’
reliance on subjective as well as objective evidence is inconsistent with the view that technology-based evidence is unbiased, more ecologically valid, and more reliable than
subjective assessment [32, 33, 60, 61]. It supports our first
principle, however, that puts an emphasis on the patientclinician relationship as a focal point of the CDSS.
This finding bears on the actual implementation of a
mHealth-based CDSS. In particular, it would be important
to identify conditions, risks and mechanisms that could give
rise to conflicting information and the impact that this could
have on disease management and patients’ care. Mechanisms
and procedures could then be put in place to deal with these
situations as well as to prevent circumstances in which clinicians are reluctant to change the treatment (as it was the
case in the presence of conflicting information from the patients and the devices in Study 3). These are situations that
can generate technical uncertainty, whereby paradoxically
the knowledge is inadequate, even if data and technology are
available [4]. Furthermore, uncertainty could be used to justify risk discounting or inaction [62, 63], mHealth based
CDSS should therefore not only provide appropriate and reliable evidence to aid clinical judgments, but also aim to reduce the uncertainty inherent in natural decision-making
contexts experienced by clinicians –when a clinician and a
patient are actually interacting.
Finally, we would like to comment on one surprising finding indicating that, at the time of the interviews, the clinicians appeared to have no ethical concerns associated with
the advent of machine learning and mHealth into their



clinical practice. Ethical judgments of clinicians are currently
covered by the established principles of medical decision
making - the Hippocratic Oath of “do no harm” and the
Helsinki declaration [64] of having appropriate oversight of
data management and the need to seek patient consent.
However, the huge advances in the field of Artificial
Intelligence and mHealth must be accompanied by rapid
education to prepare clinicians for assessing the ethical implications of using these systems in their interactions with
patients. Of particular concern is the issue of the accountability of technology – both in terms of its ability to provide
trusted and relevant information, but also in terms of its ability to recount and feedback the way in which algorithms are
providing the data for the mHealth-based CDSS (explainability). This directly links to the issue of how the assessments of
accountability and responsibility of the clinician can be established in situations where they may not be able to assess the
reliability or usefulness of information that technology provides, and when they may not be able to meaningfully assess
the consequences of their judgments. It is the latter issue that
calls for clinicians’ critical awareness of the nature of such
technology and the possible biases that may be perpetuated
throughout the life cycle of a technological system. Engaging
clinicians in these discussions is essential in order to prevent
the deterioration of patient trust and ensure effective healthcare delivery based on any future mHealth CDSS.
Future research should seek to explore the relevance of
the core principles for mHealth-based CDSS development
identified by this study in the Parkinson’s domain in other
chronic disease domains. We focused on a specific, multifaceted, and fluctuating neurodegenerative disease, but it is
possible that for each chronic-disease domain these core
principles may need to be tailored to some degree. However,
the utilisation of the theoretical and methodological framework described here would facilitate the identification of any
domain-specific issues.


Conclusions
Being guided by psychological theory enabled us to move
beyond mere information -gathering to develop core principles for designing a Parkinson’s mHealth based CDSS. We
developed a novel approach to address the questions of the
system’s core purposes, which provided a more nuanced accounting of clinician judgment in situ and helped formulate
a vision for the mHealth-based CDSS system functionalities.
This vision highlights the central importance of the patientclinician relationship in clinical decision-making and the
relevance of theoretical as opposed to algorithm (technology)-based modelling of human judgment. It challenges the
assumption that augmented decision making - based on the
operation of algorithms - is the best solution to better clinical decision making, instead establishing human decision
making as central in the increasingly machine- and datadriven world of healthcare.


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 12 of 21


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 13 of 21


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 14 of 21


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 15 of 21


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 16 of 21


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 17 of 21


Appendix 3


Table 7 Prescribing Clinicians’ User Interfaces – Proposed data requirements per goal related domains


Suggested data provision for each User Interface Domain



UI_1A UI_1B UI_1C UI_1D
Diagnosis Indicators Disease Progression Indicators Pharmacological Decision Support PwP
Safety



UI_1E
Overall QoL



Motor Symptoms Data


Tremor √ √


Muscle Rigidity √ √ √


Bradykinesia √ √ √


Gait/Postural Balance √ √ √ √


Dyskinesia √ √


On Off fluctuations/ Freezing √ √ √ √


Speech Disorder √ √


Dysphagia √ √ √


Non-motor Symptoms Data


Cognitive Disorders/Dementia √ √ √ √


Depression and Anxiety √ √ √


Impulse control disorders √ √


Sleep disorders/Daytime sleepiness √ √


Dizziness/Fainting √ √


Fatigue √


Sweating √


Urinary/ Constipation Problems √


Nausea/ Gastro-intestinal problems √


Other Supporting Data


Video of PwP symptoms √ √ √ √


Speech quality recordings √ √


Overall activity levels √ √ √ √


Number of falls/time √ √ √ √


Pain index √ √


Hallucination incidence √ √ √


Blood Pressure/time √ √ √


Bodyweight/time √


Daily fluid intake √


Adherence to care plans


Pharmacological √ √


Nutritional √ √


Physiotherapy √ √


Speech √ √


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 18 of 21


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 19 of 21


Appendix 4


Table 9 User derived requirements for PD_manager design


Requirement Details


R1 Motor and non-motor symptom outputs should be in a quick and easy to understand graphical format.


R2 Clinician needs to be able to easily identify/compare changes in symptoms overtime and drill down into different time periods
depending on the needs of the patient.


R3 Provide video capture data to help establish the difference between Dyskinesia and Tremor in patients’ self-report.


R4 Data provision should facilitate the ability to establish the co-occurrence of, and comparison of, motor with non-motor symptoms


R5 The User Interface should provide flexibility for the clinician to choose, in conjunction with the patient which symptoms and data collection
options/time periods are of most interest for a particular patient and be able to explore these in the context of a personalised integrated
data output.


R6 Provide the clinician and patient/caregiver with data on patient’s adherence to pharmacological and supporting therapy care plans over time.


R7 Provide the clinician and patient/caregiver access to an up-to-date list of a patient’s current prescribed pharmacological care plan
(e.g. drug name, format, dosage etc.).


R8 Provide the clinician and patient/caregiver with access to an up-to-date list of patient’s current prescribed supporting therapy care
plans so that they have a view of all the activities that should be taking place i.e. for a GP it would be useful to be able to see whether
a PD nurse specialist had prescribed changes to a care plan. Similarly it would be useful for a physiotherapist to be able to see what
occupational therapy plans had been prescribed etc. thus facilitating a better understanding of the overall care being provided across
the multidisciplinary team (MDT).


R9 Provide the clinician with the ability to monitor the effectiveness of the step-by-step changes made to pharmacological care plans
both at and between face-to-face consultations (i.e. remotely) to establish if the change has resulted in a positive/negative outcome.


R10 Provide the clinician and patient/caregivers with the ability to access data on patient’s activity levels/duration in their home environment.


R11 Provide the clinician with the ability to prescribe supporting therapies a patient can engage with at home and provide data on
patient’s adherence/performance indicators when they have engaged with these therapies via the PD_manager platform (e.g.
gamification of physio, cognitive activities, speech and nutrition).


R12 Provide a communication platform to facilitate the sharing of information and alerts between clinicians participating in the care of a
patient in the context of an MDT.


R13 Provide functionality to alert patient/caregiver with when they should take their medication.



Abbreviations
CDSS: Clinical Decision Support System; HTA: Hierarchical Task Analysis;
HTD: Hierarchical Task Diagram; mHealth: Mobile Health; MRI: Magnetic
Resonance Imagery; PD: Parkinson’s Disease; QoL: Quality of Life; QoS: Quality
of Service


Acknowledgements
The authors thank all clinicians who participated in the study. The work of
the authors was supported by the PD_Manager Project.


Authors’ contributions
LT has an overall responsibility for the study delivery. LT, CEH, AB, PR, BE, MP,
ES, MMLT and HG have conceived the study and developed the protocol.
CEH, AB, PR, CP, GS, FA, MG, AM, GG, IC, SK; DG and DF collected and
analysed the data. LT, CEH, AB, PR, BE, MP and ES wrote up the article. All
authors reviewed the article. All authors have approved the manuscript
being submitted.


Funding
PD_Manager is a research project funded by the European Commission under the
Framework Programme for Research and Innovation Horizon 2020 programme,
specifically the PHC-26 (Personalising Health and Care-26) topic - ‘Self-management
of health and disease: citizen engagement and mHealth aimed at empowering citizens to manage their own health and disease’ - Grant Agreement: 643706 —
mhealth platform for Parkinson’s disease management (PD_manager).
The research is sponsored in: England by the University of Surrey, Guildford,
GU2 7XH; Greece by the University of Ioannina, P.O. Box 1186, 45110
Ioannina; Italy by Fondazione Santa Lucia, Via Ardeatina, 306/354, 00142
Rome RM and San Camillo / IRCCS Hospital Foundation, Via Alberoni, 70,
30126 Lido Venice VE.
Neither the funding body, nor the sponsors, have any role in: the design of
the study; the collection, analysis and interpretation of data; writing of the
manuscript; decision to submit the report for publication.



Availability of data and materials
The datasets generated and/or analysed during the current study are not
publicly available. This is because the written consent from the participants
to re-purpose the anonymised data was given under the condition that the
data would only be made available if relevant legal, professional and ethical
approvals were provided. Anonymised data is available from the corresponding author on reasonable request.


Ethics approval and consent to participate
Since the three studies collected data from clinicians (not patients), a formal
ethical approval was not required within any of the national legislations (UK,
Greece, Slovenia and Italy). However, within the UK, Research &
Development approval from the hospital trusts - the two hospitals that
allowed access to the clinicians - was obtained. For each study, written
Informed Consent was obtained from the participants.


Consent for publication
Not Applicable.


Competing interests
The authors declare that they have no competing interests.


Author details
1Faculty of Health and Medical Sciences, University of Surrey, Guildford, UK.
2Department of Psychology, University of Bournemouth, Bournemouth, UK.
3Department of Neurorehabilitation, Fondanzione Santa Lucia, Rome, Italy.
4Fondanzione Ospedale San Camillo (I.R.C.C.S.), Parkinson’s Department
Institute of Neurology, Venice, Italy. [5] University Rehabilitation Institute,
Republic of Slovenia, Soča, Ljubljana, Slovenia. [6] Department of Material
Sciences and Engineering, University of Ioannina, Ioannina, Greece.
7Nurology, Faculty of Medicine, School of Health Sciences, University of
Ioannina, Ioannina, Greece.


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 20 of 21



Received: 12 April 2019 Accepted: 20 January 2020


References
1. Kay M, Santos J, Takane M. mHealth: new horizons for health through
mobile technologies. World Health Organization. 2011;64:66–71.
2. World Health Organization. mHealth. Use of appropriate digital technologies
for public health: report by Director-General. 71st World Health Assembly
provisional agenda item, 12, A71. 2018.
3. Bradway M, Carrion C, Vallespin B, Saadatfard O, Puigdomènech E,
Espallargues M, Kotzeva A. mHealth assessment: conceptualization of a
global framework. JMIR mHealth uHealth. 2017;5:e60.
4. Beresford EB. Uncertainty and the shaping of medical decisions. Hastings
Cent Rep. 1991;21:6–11.
5. Bhise V, Rajan SS, Sittig DF, Morgan RO, Chaudhary P, Singh H. Defining and
measuring diagnostic uncertainty in medicine: a systematic review. J Gen
Intern Med. 2018;33:103–15.
6. Dalton AF, Golin CE, Esserman D, Pignone MP, Pathman DE, Lewis CL.
Relationship between physicians’ uncertainty about clinical assessments and
patient-centered recommendations for colorectal cancer screening in the
elderly. Med Decis Mak. 2015;35:458–66.
7. Eddy DM. Variations in physician practice: the role of uncertainty. Health Aff.
1984;3:74–89.
8. Han PK, Klein WM, Arora NK. Varieties of uncertainty in health care: a
conceptual taxonomy. Med Decis Mak. 2011;31:828–38.
9. Kaplan RM, Frosch DL. Decision making in medicine and health care. Annu
Rev Clin Psychol. 2005;1:525–56.
10. Seely AJ. Embracing the certainty of uncertainty: implications for health care
and research. Perspect Biol Med. 2013;56:65–77.
11. Tait RC, Chibnall JT, Kalauokalani D. Provider judgments of patients in pain:
seeking symptom certainty. Pain Med. 2009;10:11–34.
12. Chaudhry B, Wang J, Wu S, Maglione M, Mojica W, Roth E, Morton SC,
Shekelle PG. Systematic review: impact of health information
technology on quality, efficiency, and costs of medical care. Ann Intern
Med. 2006;144:742–52.
13. Buntin MB, Burke MF, Hoaglin MC, Blumenthal D. The benefits of health
information technology: a review of the recent literature shows
predominantly positive results. Health Aff. 2011;30:464–71.
14. Sim I, Gorman P, Greenes RA, Haynes RB, Kaplan B, Lehmann H, Tang PC.
Clinical decision support systems for the practice of evidence-based
medicine. J Am Med Inform Assoc. 2001;8:527–34.
15. Bates DW, Cohen M, Leape LL, Overhage JM, Shabot MM, Sheridan T.
Reducing the frequency of errors in medicine using information
technology. J Am Med Inform Assoc. 2001;8:299–308.
16. Teich JM, Wrinn MM. Clinical decision support systems come of age. MD
Comput. 2000;17:43–6.
17. Jones SS, Rudin RS, Perry T, Shekelle PG. Health information technology: an
updated systematic review with a focus on meaningful use. Ann Intern
Med. 2014;160:48–54.
18. Free C, Phillips G, Galli L, Watson L, Felix L. The effectiveness of Mobilehealth technology-based health behaviour change or disease; 2013.
19. Gagnon M-P, Ngangue P, Payne-Gagnon J, Desmartis M. m-health adoption
by healthcare professionals: a systematic review. J Am Med Inform Assoc.
2015;23:212–20.
20. Bright TJ, Wong A, Dhurjati R, Bristow E, Bastian L, Coeytaux RR, Samsa G,
Hasselblad V, Williams JW, Musty MD. Effect of clinical decision-support
systems: a systematic review. Ann Intern Med. 2012;157:29–43.
21. Peleg M, Shachak A, Wang D, Karnieli E. Using multi-perspective
methodologies to study users’ interactions with the prototype front end of
a guideline-based decision support system for diabetic foot care. Int J Med
Inform. 2009;78:482–93.
22. Jacobson I, Christerson PJP. and Övergaard G. (1992) A use case driven
approach. Addison-Wesley Publishing Company; 1992.
23. Tsiouris KM, Gatsios D, Rigas G, Miljkovic D, Seljak BK, Bohanec M,
Arredondo MT, Antonini A, Konitsiotis S, Koutsouris DD. PD_Manager: an
mHealth platform for Parkinson's disease patient management. Healthc
Technol Lett. 2017;4:102–8.
24. Serrano JA, Larsen F, Isaacs T, Matthews H, Duffen J, Riggare S, Capitanio F,
Ferreira JJ, Domingos J, Maetzler W. Participatory design in Parkinson's
research with focus on the symptomatic domains to be measured. J Park
Dis. 2015;5:187–96.



25. Dua T. Atlas: country resources for neurological disorders 2004: results of a
collaborative study of the World Health Organization and the world
Federation of Neurology: World Health Organization; 2004.
26. Dorsey E, Constantinescu R, Thompson J, Biglan K, Holloway R, Kieburtz K,
Marshall F, Ravina B, Schifitto G, Siderowf A. Projected number of people
with Parkinson disease in the most populous nations, 2005 through 2030.
Neurology. 2007;68:384–6.
27. Mirza F, Norris T, Stockdale R. Mobile technologies and the holistic
management of chronic diseases. Health Inform J. 2008;14:309–21.
28. Dietvorst BJ, Simmons J, Massey C. Understanding Algorithm Aversion:
Forecasters Erroneously Avoid Algorithms After Seeing them Err. In:
Academy of Management Proceedings. NY: Academy of Management
Briarcliff Manor; 2014. p. 12227.
29. Eysenbach G, Diepgen TL. The role of e-health and consumer health
informatics for evidence-based patient choice in the 21st century. Clin
Dermatol. 2001;19:11–7.
30. Hurt CS, Cleanthous S, Newman SP. Further explorations of illness
uncertainty: carers’ experiences of Parkinson’s disease. Psychol Health. 2017;
32:549–66.
31. Yaacob S, Muthusamy H, Sarillee M, Lee CH, Basah SN, Oung QW, Lee HL.
Technologies for Assessment of motor disorders in Parkinson’s disease: a
review; 2015.
32. Del Din S, Godfrey A, Mazzà C, Lord S, Rochester L. Free-living monitoring
of Parkinson's disease: lessons from the field. Mov Disord. 2016;31:1293–313.
33. Maetzler W, Domingos J, Srulijes K, Ferreira JJ, Bloem BR. Quantitative
wearable sensors for objective assessment of Parkinson's disease. Mov
Disord. 2013;28:1628–37.
34. Yang K, Xiong WX, Liu FT, Sun YM, Luo S, Ding ZT, Wu JJ, Wang J. Objective
and quantitative assessment of motor function in Parkinson’s disease—from
the perspective of practical applications. Ann Transl Med. 2016;4(5):90.
35. Koerts J, Tucha L, Leenders KL, van Beilen M, Brouwer WH, Tucha O.
Subjective and objective assessment of executive functions in Parkinson's
disease. J Neurol Sci. 2011;310:172–5.
36. Toosizadeh N, Mohler J, Lei H, Parvaneh S, Sherman S, Najafi B. Motor
performance assessment in Parkinson’s disease: association between
objective in-clinic, objective in-home, and subjective/semi-objective
measures. PLoS One. 2015;10:e0124763.
37. Tzallas AT, Tsipouras MG, Rigas G, Tsalikakis DG, Karvounis EC, Chondrogiorgi
M, Psomadellis F, Cancela J, Pastorino M, Waldmeyer MTA. PERFORM: a
system for monitoring, assessment and management of patients with
Parkinson’s disease. Sensors. 2014;14:21329–57.
38. Samà A, Pérez-López C, Rodríguez-Martín D, Moreno-Aróstegui JM, Rovira J,
Ahlrichs C, Castro R, Cevada J, Graça R, Guimarães V. A double closed loop
to enhance the quality of life of Parkinson's disease patients: REMPARK
system. Innov Med Healthc. 2015;207:115–24.
39. Ferreira JJ, Godinho C, Santos AT, Domingos J, Abreu D, Lobo R, Gonçalves
N, Barra M, Larsen F, Fagerbakke Ø. Quantitative home-based assessment of
Parkinson’s symptoms: the SENSE-PARK feasibility and usability study. BMC
Neurol. 2015;15:89.
40. Bohanec M, Miljković D, Valmarska A, Mileva Boshkoska B, Gasparoli E,
Gentile G, Koutsikos K, Marcante A, Antonini A, Gatsios D, Rigas G. A
decision support system for Parkinson disease management: expert
models for suggesting medication change. J Decis Syst. 2018;27(sup1):
164–72.
41. Diaper D. Understanding task analysis for human-computer interaction. The
handbook of task analysis for human-computer interaction; 2004. p. 5–47.
42. Brehmer B, Joyce CRB. Human judgment: the SJT view: Elsevier; 1988.
43. Skånér Y, Bring J, Ullman B, Strender L-E. The use of clinical information in
diagnosing chronic heart failure: a comparison between general
practitioners, cardiologists, and students. J Clin Epidemiol. 2000;53:1081–8.
44. Kirwan J, Currey H, Brooks P. Measuring Physicians’ judgment: the use of
clinical data by Australian rheumatologists. Aust NZ J Med. 1985;15:738–44.
45. Kee F, Patterson CC, Wilson AE, McConnell JM, Wheeler SM, Watson JD.
Judgment analysis of prioritization decisions within a dialysis program in
one United Kingdom region. Med Decis Mak. 2002;22:140–51.
46. Cabestany J, López CP, Sama A, Moreno JM, Bayes A, Rodriguez-Molinero A.
REMPARK: When AI and technology meet Parkinson Disease assessment. In
Proceedings of the 20th International Conference Mixed Design of
Integrated Circuits and Systems-MIXDES 2013. IEEE. 2013:562–7.
47. Wigton RS. Social judgement theory and medical judgement. Think Reason.
1996;2:175–90.


Timotijevic et al. BMC Medical Informatics and Decision Making      (2020) 20:34 Page 21 of 21


48. Shanteau J, Edwards W, Hall B. Decision making by experts: Influence of five
key psychologists. New York: Psychology Press; 2015. p. 3–26.
49. Chibnall JT, Tait RC, Ross LR. The effects of medical evidence and pain
intensity on medical student judgments of chronic pain patients. J Behav
Med. 1997;20:257–71.
50. Igier V, Mullet E, Sorum PC. How nursing personnel judge patients’ pain. Eur
J Pain. 2007;11:542–50.
51. Rusconi P, Riva P, Cherubini P, Montali L. Taking into account the observers’
uncertainty: a graduated approach to the credibility of the patient’s pain
evaluation. J Behav Med. 2010;33:60–71.
52. Goetz CG, Poewe W, Rascol O, Sampaio C, Stebbins GT, Counsell C, Giladi N,
Holloway RG, Moore CG, Wenning GK. Movement Disorder Society task
force report on the Hoehn and Yahr staging scale: status and
recommendations the Movement Disorder Society task force on rating
scales for Parkinson's disease. Mov Disord. 2004;19:1020–8.
53. Shiner T, Seymour B, Symmonds M, Dayan P, Bhatia KP, Dolan RJ. The effect
of motivation on movement: a study of bradykinesia in Parkinson’s disease.
PLoS One. 2012;7:e47138.
54. Postuma RB, Berg D, Stern M, Poewe W, Olanow CW, Oertel W, Obeso J,
Marek K, Litvan I, Lang AE. MDS clinical diagnostic criteria for Parkinson's
disease. Mov Disord. 2015;30:1591–601.
55. Braun V, Clarke V. Using thematic analysis in psychology. Qual Res Psychol.
2006;3:77–101.
56. Castro J, Kolp M, Mylopoulos J. Towards requirements-driven information
systems engineering: the Tropos project. Inf Syst. 2002;27:365–89.
57. Charles C, Gafni A, Whelan T. Shared decision-making in the medical
encounter: what does it mean? (or it takes at least two to tango). Soc Sci
Med. 1997;44:681–92.
58. Elwyn G, Edwards A, Kinnersley P, Grol R. Shared decision making and the
concept of equipoise: the competences of involving patients in healthcare
choices. Br J Gen Pract. 2000;50:892–9.
59. Siadat S, Ferreira AM, Khoei TT, Ghapanchi AR. Performance analysis of QoSbased web service selection through integer programming. World Appl Sci
J. 2013;28(4):463–72.
60. Hobert MA, Maetzler W, Aminian K. Chiari: Technical and clinical view on
ambulatory assessment in Parkinson’s disease. Acta Neurol Scand. 2014;130:
[139–47. https://doi.org/10.1111/ane.12248.](https://doi.org/10.1111/ane.12248)
61. Godinho C, Domingos J, Cunha G, et al. A systematic review of the
characteristics and validity of monitoring technologies to assess Parkinson’s
[disease. J Neuroeng Rehabil. 2016;13:1–11. https://doi.org/10.1186/s12984-](https://doi.org/10.1186/s12984-016-0136-7)
[016-0136-7.](https://doi.org/10.1186/s12984-016-0136-7)
62. Kuhn KM. Message format and audience values: interactive effects of
uncertainty information and environmental attitudes on perceived risk.
[J Environ Psychol. 2000;20:41–51. https://doi.org/10.1006/jevp.1999.0145.](https://doi.org/10.1006/jevp.1999.0145)
63. Barnett J, Timotijevic L, Vassallo M, Shepherd R. Precautionary advice about
mobile phones: public understandings and intended responses. J Risk Res.
[2008;11:525–40. https://doi.org/10.1080/13669870802086430.](https://doi.org/10.1080/13669870802086430)
64. Varga A. Declaration of Helsinki (Adopted by the 18th world medical
assembly in Helsinki, Finland, and revised by the 29th world medical
assembly in Tokyo, 1975): The main issue in bioethics; 1984.


Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional affiliations.


