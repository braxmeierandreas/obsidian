Schütze _et al._
_BMC Medical Informatics and Decision Making     (2023) 23:144_
https://doi.org/10.1186/s12911-023-02245-w



BMC Medical Informatics and
Decision Making


## **RESEARCH Open Access**
# Requirements analysis for an AI‑based clinical decision support system for general practitioners: a user‑centered design process

Dania Schütze [1*] [, Svea Holtz](http://orcid.org/0000-0003-4788-2082) [1] [, Michaela C. Neff](http://orcid.org/0000-0002-4477-701X) [2] [, Susanne M. Köhler](http://orcid.org/0000-0003-4286-7959) [1] [, Jannik Schaaf](http://orcid.org/0000-0002-4255-1770) [2] [,](http://orcid.org/0000-0002-0058-155X)
Lena S. Frischen [3], Brita Sedlmayr [4] [and Beate S. Müller](http://orcid.org/0000-0001-6159-7822) [1,5]


**Abstract**
**Background** As the first point of contact for patients with health issues, general practitioners (GPs) are frequently
confronted with patients presenting with non-specific symptoms of unclear origin. This can result in delayed, prolonged or false diagnoses. To accelerate and improve the diagnosis of diseases, clinical decision support systems
would appear to be an appropriate tool. The objective of the project ‘Smart physician portal for patients with unclear
disease’ (SATURN) is to employ a user-centered design process based on the requirements analysis presented in this
paper to develop an artificial Intelligence (AI)-based diagnosis support system that specifically addresses the needs
of German GPs.
**Methods** Requirements analysis for a GP-specific diagnosis support system was conducted in an iterative process
with five GPs. First, interviews were conducted to analyze current workflows and the use of digital applications
in cases of diagnostic uncertainty (as-is situation). Second, we focused on collecting and prioritizing tasks to be performed by an ideal smart physician portal (to-be situation) in a workshop. We then developed a task model with corresponding user requirements.
**Results** Numerous GP-specific user requirements were identified concerning the tasks and subtasks: performing
data entry (open system, enter patient data), reviewing results (receiving and evaluating results), discussing results
(with patients and colleagues), scheduling further diagnostic procedures, referring to specialists (select, contact, make
appointments), and case closure. Suggested features particularly concerned the process of screening and assessing
results: e.g., the system should focus more on atypical patterns of common diseases than on rare diseases only, display probabilities of differential diagnoses, ensure sources and results are transparent, and mark diagnoses that have
already been ruled out. Moreover, establishing a means of using the platform to communicate with colleagues
and transferring patient data directly from electronic patient records to the system was strongly recommended.
**Conclusions** Essential user requirements to be considered in the development and design of a diagnosis system
for primary care could be derived from the analysis. They form the basis for mockup-development and system
engineering.
**Keywords** Clinical decision support systems, Computer-assisted diagnosis, Primary care, User-centered design,
Qualitative research, Requirements analysis


*Correspondence:
Dania Schütze
schuetze@allgemeinmedizin.uni-frankfurt.de
Full list of author information is available at the end of the article


© The Author(s) 2023. **Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or
other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this
[licence, visit http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/. The Creative Commons Public Domain Dedication waiver (http://​creat​iveco​](http://creativecommons.org/licenses/by/4.0/)
[mmons.​org/​publi​cdoma​in/​zero/1.​0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.](http://creativecommons.org/publicdomain/zero/1.0/)


Schütze _et al. BMC Medical Informatics and Decision Making     (2023) 23:144_ Page 2 of 10



**Background**
General practitioners (GPs) are the first point of contact
for patients with health issues in many countries. Frequently, patients consult their GPs with ambiguous symptoms of unknown origin [1]. Although having a common
disease, such patients may also present with atypical or
non-specific symptoms [2]. Furthermore, symptoms
may vary between men and women, which can lead to
diagnostic uncertainty [3–6]. At the same time, patients
with ambiguous symptoms may be suffering from a rare
disease [2, 7]. According to current estimates, 5,000 to
8,000 rare diseases exist [8, 9]. The European Union considers a disease as rare when it affects no more than 1 in
2,000 persons and estimates that about 30 million people in Europe are affected [9]. Diagnosing a rare disease
can often take years, during which uncertainty, emotional and physical burden, false diagnoses and numerous physician consultations are the norm [7, 10–12] and
even after years, many cases remain unclear [13]. When
symptom complexes are ambiguous or unfamiliar to the
physician, clinical decision support systems (CDSS) can
help GPs form a diagnosis and make a decision [14–16].
According to Sim et al., a CDSS is defined as ‘software
designed to be a direct aid to clinical decision-making,
in which the characteristics of an individual patient are
matched to a computerized clinical knowledge base and
patient-specific assessments or recommendations are
then presented to the clinician or the patient for a decision’ [17]. Several CDSS are used in primary care, mainly
for screening and diagnosing common chronic diseases.
Research shows that CDSS have the potential to improve
and accelerate the diagnosis [14]. However, little is known
about the use of CDSS for acute and uncommon diseases
in primary care [14]. Studies have identified several barriers and challenges to CDSS and their use, such as poor
workflow integration, a lack of acceptance or trust, and
poor usability [14, 15, 18–21]. To address these barriers
and establish CDSS as a means of helping GPs form a
diagnosis when confronted with unclear disease patterns
in primary care, a user-centered approach needs to be
taken in the development of future systems [14, 20–22].
The objective of the ‘Smart physician portal for patients
with unclear disease’ (SATURN) project funded by the
German Federal Ministry of Health, is to develop an Artificial Intelligence (AI)-based diagnosis support tool for
GPs. The medical focus thereby is on making a diagnosis
in cases of diagnostic uncertainty. On a technical level,
rule-based systems, machine learning, and case-based
reasoning will be employed. A rule-based system can be
used to make a diagnosis based on guidelines. Machine
learning allows a diagnosis to be predicted with a statistical probability, while case-based reasoning identifies
similar patient cases from a case base and presents them



to the user. Existing CDSS generally use only one method
of decision support [22].
To ensure that the diagnosis tool meets the needs
of future users, is widely accepted, and shows a good
usability, GPs will be continuously involved in the usercentered design (UCD) process. UCD is an engineering
strategy that, when developing interactive systems, investigates and focuses on the needs, desires, and limitations
of end users. Information on the context of use is therefore collected, and an analysis of user requirements is
carried out [23–28].
In this paper, we present the user requirements analysis we conducted with GPs as the first step in the development of an AI-based CDSS in German primary care.
The objectives of the requirements analysis were (1) to
investigate diagnostic workflows and (2) to find out what
a new CDSS must provide from the user’s perspective.


**Methods**
**Design**
As part of the UCD, we used a qualitative design to
conduct requirements analysis with a group of general practitioners [27, 29]. We carried out interviews to
gain insight into current workflows (as-is situation) [26,
29, 30], and conducted a workshop to collect ideas, and
identify needs and user requirements for a new CDSS
for GPs (to-be situation) [31]. As a result, we developed a
task model and identified user requirements for the new
system. A task model is a summary of the tasks and subtasks that users will perform with the support of the new
or revised interactive system [29]. User requirements
describe what an interactive system should enable users
to do in order to achieve their goals [29, 32].
In the following sections, we describe the process in
detail. Figure 1 shows the different steps of collecting
data and obtained results.
The study was performed and reported in accordance
with the Consolidated Criteria for Reporting Qualitative
Research (COREQ) [33].


**Setting and sampling**
First, the project team jointly defined and roughly
characterized the target group for the CDSS. We then
used a purposeful sampling approach [34] to constitute a group of five general practitioners to accompany the entire project. This group size is common
because it already enables a high degree of usability
to be achieved. This is especially true when the project is expected to involve multiple iterations [35–37].
We recruited male and female physicians and ensured
they had a basic understanding of digitization. The participants were known to us through previous research


Schütze _et al. BMC Medical Informatics and Decision Making     (2023) 23:144_ Page 3 of 10


**Fig. 1** Design of requirements analysis and results



projects on other topics. They were contacted by email,
received written information on the study and provided
their written informed consent.


**Data collection**
_**Interviews**_
A team of researchers from the fields of sociology,
medicine, medical sciences and medical informatics
prepared an interview guide addressing the research
question ‘How do general practitioners currently deal
with cases of patients with ambiguous symptoms of
unknown origin?’ The guide was presented in an interdisciplinary research group for qualitative methods at
the Frankfurt Institute of General Practice, where it
was discussed and adapted. The interview guide was
also tested in three pretest interviews. The final guide
(see Additional file 1) contained questions on the following topics: 1. Current workflow in cases of diagnostic uncertainty, 2. Use of digital applications in cases
of diagnostic uncertainty, 3. Experience in the diagnosis of rare diseases, 4. Additional comments. Moreover, information was collected on age, number of years
working in general practice, additional qualifications,
employment status and the technical equipment available in the practice.
From March to May 2022, a researcher (SH) with a
medical background and experience in qualitative
methods interviewed the five participants by telephone.
The length of the interviews ranged from 24 to 44 min.
All interviews were audio-taped and transcribed in a
paraphrased form. Selected passages were transcribed
verbatim as quotations. Participants provided their verbal consent to be audio recorded at the beginning of the
interview.



_**Workshop**_
In June 2022, we conducted a workshop with all five participating GPs to gather ideas and find out about user
needs for a new CDSS for general practitioners. The
workshop was performed online via Zoom and lasted for
two hours. It was hosted by three study team researchers from the fields of medicine (SH), medical informatics (MN), sociology and medical sciences (DS). One
researcher moderated the discussion, one took notes on
the shared Zoom-whiteboard and one provided background information on the project, took notes and provided technical support. The participants were first told
about the current status of the project, as well as the
aim and structure of the workshop. We then conducted
a brainstorming on the question: ‘What tasks would you
like to perform with an ideal smart physician system for
unclear diagnoses?’ The answers (ideas) were numbered
and documented on the shared Zoom-whiteboard.
After the brainstorming, the participants were asked
to name their top 5 ideas in the form of a template [37]
that we provided via email. The template consisted of
the following fields: 1. The number of the idea, 2. The
name of the idea, 3. A brief description of the idea, and
4. Why this idea was important to them. All participants
returned the completed template with their prioritized
ideas by email. We ended the workshop with an opportunity for questions and a preview of the next steps in the
project.


**Data analysis**
_**Interviews**_
Three researchers (SH, MN, DS) transcribed the interviews in paraphrased form and analyzed them [29]. Each
interview was first paraphrased by one person. A second


Schütze _et al. BMC Medical Informatics and Decision Making     (2023) 23:144_ Page 4 of 10



researcher listened to the interview, reviewed the transcript
and made additions where necessary. Following the method
described by Geis and Polkehn [27, 29], we first derived user
needs from the transcripts. These were phrased according
to the following syntax rule: _The user must have_ < _resource/_
_information/…_ - _to_ < _make decision_ - _or_ < _execute action_ - . In
the next step, we formulated user requirements based on the
user needs, describing what users must be able to do with
the system: _The_ < _user_ - _needs to be able to_ < _recognize/enter/_
_select/…_ - _in the system_ . Table 1 shows an example. Thereafter, all results were checked and discussed by the study
team and an overall list of user requirements was compiled
(see Additional file 2). Finally, the user requirements were
structured by identifying tasks and subtasks they referred
to. These formed an initial task model that outlined the as-is
situation [29]. In addition, a so-called proto-persona for the
primary target group of ‘general practitioners’ was developed from assumptions and existing knowledge about the
target group, and supplemented with details from the interviews. The persona aimed to create a uniform understanding of the target group in the project team in order to better
prioritize development goals later on [38, 39].


_**Workshop and synthesis**_
As in the case of the interviews, we derived user requirements from the user needs expressed in the workshop
with respect to a to-be situation and added them to the
list of requirements. As some needs led to new tasks, we
extended the task model so that it now represented the
to-be situation.


**Table 1** Example for derivation of user requirements from interviews



**Results**
**Participants**
Five GPs participated in the requirements analysis.
The characteristics of the participants can be found in
Table 2.


**User group**
Even though the project was designed with GPs in mind,
the inclusion of healthcare assistants as a second user group
would have been conceivable. However, it became apparent
during the interviews that healthcare assistants were not
part of the diagnostic workflow and thus would not be users
of the system. The persona (Additional file 3) therefore represents the main user group of general practitioners.


**User requirements**
In the interviews, the GPs described how they currently proceed in cases of diagnostic uncertainty and
what digital and non-digital support options they
typically use (including their advantages and disadvantages), as well as what they are currently missing.
In the workshop, we collected ideas for a new CDSS.
We created a task model according to the workflow
and assigned requirements to it. The task model initially represented the results of the interviews and was
later supplemented by the results of the workshop (see
Fig. 2; steps 3 and 6 were added after the workshop).
In the following, we report on the most important user
requirements for each step of the task model. For better
readability, we do not use the syntax employed in the



**Paraphrased part of the interview** **User need (N)** **User requirement (UR)**



In a case of suspected Fabry-disease, GP02 performed tests that she researched and ordered
on the Internet herself. Her suspicion was ultimately not confirmed

When GP05 looks at the results of a Google
search, much of what is suggested has already
been ruled out by examinations. GP05 then
looks at what remains, and what has not yet
been investigated but that seems reasonable


**Table 2** Participant characteristics



N: The physician needs to know what tests UR: The physician needs be able to recognize
to perform to rule out or confirm a diagnosis in the system what tests he/she needs to confirm
a suspected diagnosis



N: The physician needs to be able to sort
suspected diagnoses based on which diagnoses
have already been ruled out



UR: The physician needs to be able to exclude
diagnoses in the system



**ID** **Age** **m/f** **Additional qualifications or special focus** **Time working in** **Employment status**
**general practice**


1 43 m Emergency care, focus on geriatrics and palliative care 9 years self-employed

2 44 f Intensive and emergency care 6 years employed

3 33 m None 9 months employed

4 49 m Diabetologist, nephrologist, focus on hypertensiology 8 years self-employed
and nutritional medicine

5 35 f Focus on rare diseases 2.5 years employed


Schütze _et al. BMC Medical Informatics and Decision Making     (2023) 23:144_ Page 5 of 10


**Fig. 2** Task model for use of CDSS by GPs



analysis in the presentation of results, but report the
requirements narratively and substantiate them with
quotes from the interviews (I), the workshop (WS) and
the Top 5 booklets provided by the participants.


_**Perform data entry**_
In the interviews, it became clear that basic requirements would have to be fulfilled before physicians
could use the system at all. In general, it should be possible to use the system on different devices and with
different operating systems. Physicians also need to be
able to use it in parallel with practice management software and other colleagues.
The GPs named various essential data entry options
for test results and information that they use for
research, or that they would like to use in the future.
These were: medical findings, vague descriptions of
complaints, tentative diagnoses, family anamneses, laboratory parameters, symptoms and especially combinations of symptoms:

_Well what I think would probably be useful – […]_
_you can directly enter a number of symptoms_
_together – that’s rather practical of course because_
_diagnoses generally differ as a result of specific_
_symptom combinations. (I, GP3)_

Furthermore, the user needs to be able to enter the
parameters weight, age and gender, as such information
is essential when making a diagnosis:

_Well the combination of ‘[…] I have a symptom,_
_which might even be a leading symptom and well,_
_I can filter out the probable diagnoses according to_
_sex, age, or age group‘. (I, GP3)_

In this regard, it became evident that GPs would
much prefer to simply transfer sociodemographic and
patients’ medical data from the practice management



system to the CDSS rather than enter them manually,
as it would save time and reduce possible transmission
errors.
Another outcome of the workshop was that GPs would
like to create patient records in the system, which they
could then access and rework at any time:


Excerpt from a Top 5 booklet:
Name of the idea:

_Create patient record that is possible to update._
Description of the idea:

_Save information that has already been entered_
_so that you can continue to work on it later._

Why is this important to you?

_So that I can work on the case again and again_
_and add new information later; to save me work_
_(to avoid doing the same thing over and over_
_again). (Top 5 booklet, GP2)_

The participants also pointed out that in a best case
scenario, suggestions for entries would be made automatically during the data entry process, perhaps in the form
of an intelligent query, which would help in recognizing
what further data and test results should be entered.


_**Review results**_
An important step that was highlighted in the interviews
was the screening and assessment of results. GPs emphasized that in a primary care setting, the CDSS should not
focus exclusively on rare diseases, but should also consider common diseases. This became obvious in the criticism of a ‘symptom checker’ that already existed:

_The end result is that the extent of a symptom match_
_with certain diagnoses is given in percentage terms._
_And then my feeling was that the usual diagnoses_


Schütze _et al. BMC Medical Informatics and Decision Making     (2023) 23:144_ Page 6 of 10



_you make in family practice didn’t play a role but_
_that it was more like rare diseases were matched. I_
_would say that our classic [diagnoses], the ones that_
_occur a lot – there wasn’t really a match for them._
_(I, GP1)_

To assess the results, it was essential for the participants to see which differential diagnoses should be
considered:

_When I’m stuck with a patient, I would just like a_
_portal with a straightforward user interface that_
_permits me to simply enter symptoms and medical_
_findings or diagnoses as keywords so that the system_
_ultimately just provides me with differential diagno-_
_ses. (WS, GP4)_

At the same time, the GPs would like to be able to manually hide diagnoses that have already been ruled out by
previous tests from the list of results:
Description of the idea:

_In the results section, I would like to be able to ‘gray_
_out’ all suggested diagnoses that have already been_
_ruled out._

Why is this important to you?

_Leads to more clarity—one could focus on the_
_remaining diagnoses. The system could learn from_
_this. (Top 5 booklet, GP5)_

In order to be able to evaluate the results, participants
recommended that the probability of specific diagnoses
be provided:

Description of the idea:


_There are different ways in which search results could_
_be sorted, e.g. alphabetically, by date of inclusion in_
_the database or similar. The most sensible way would_
_be a ‘best-match’ for the given search parameters, if_
_possible with an indication of probability._

Why is this important to you?

_Makes it easier to focus on the most relevant diag-_
_noses of all the different possibilities. (Top 5 book-_
_let, GP3)_

In addition, the participants thought the user needed to
be able to identify the source of the provided information:
Description of the idea:

_Details on the source of [the information on] a par-_
_ticular diagnosis that the system provides should_
_be provided, along with the guideline/expert_
_knowledge, etc., on which the portal is based._



Why is this important to you?


_Transparency, and so I can check whether I con-_
_sider the source to be reliable. It might also be_
_important to re-read it. (Top 5 booklet, GP5)_

Ideally, users should also have free access to the provided information.


_**Discuss results**_
In the workshop, it became clear that the GPs would like
to be able to share their initial thoughts and results with
patients and colleagues. GPs wanted the system to provide a platform through which they could communicate
with colleagues when cases were unclear:
Description of the idea:

_It should be possible to communicate live—in a kind_
_of forum—with colleagues, experts should also par-_
_ticipate and contribute to the solution of the problem._

Why is this important to you?

_The AI is refined –‘fed’–with NI (Natural Intelli-_
_gence). (Top 5 booklet, GP4)_

In this context, some participants raised the idea of giving patients access to their own patient records in the
CDSS:

_Just so the patient has the chance to follow what’s_
_going on, like when patients are transferred to spe-_
_cialists who then receive a copy of the report or_
_something like that. […] So that they can also inter-_
_vene and correct certain things - if he sees that I have_
_described something differently to the way he would,_
_perhaps the symptoms, for example. (WS, GP4)_

Other participants were critical of this suggestion and
recommended restricting access:

_If patients did have the chance to enter data or_
_symptoms themselves, I think it would be impor-_
_tant that it was possible to activate or dis-activate_
_patient access because when I think of certain_
_patients, who get completely carried away and can’t_
_focus at all, which can make consultations very_
_confusing […] That‘s why I wouldn’t like it if every_
_patient had access. (WS, GP2)_


_**Schedule further diagnostics**_
When the system has generated several results, users
need to be able to confirm or rule out differential diagnoses. For example, the GP might need information on


Schütze _et al. BMC Medical Informatics and Decision Making     (2023) 23:144_ Page 7 of 10



which tests he or she would need in order to diagnose a
rare disease:

_A further step that I think would be rather nice would_
_be to be told which diagnostic procedures could be_
_used to confirm or rule out the differential diagnoses_
_that the system identifies because I thought that was_
_a big problem with ADA Health [a symptom checker_
_app]. You‘re shown at the end, in percentage terms,_
_what diagnoses could explain it, but for me, one step_
_further would be to receive an indication, okay, how_
_can I best confirm or rule out the diagnosis. (WS, GP4)_


_**Refer to specialist**_
When the GPs would like to refer the patient to a specialist for further diagnostic tests, they would like the system
to recommend the most appropriate physician to contact
for a specific suspected diagnosis. If suitable information
platforms already exist for this purpose, the user should
be forwarded to them:

Description of the idea:


_The portal should link to existing solutions, e.g. SE-_
_Atlas [Care atlas for people with rare diseases],_
_Orphanet, etc._


Why is this important to you?


_You don’t have to reinvent everything. Resources that_
_already exist should be used and linked to. If the por-_
_tal is widely used, it might increase the visibility of_
_existing structures like SE-Atlas. (Top 5 booklet GP1)_

In addition, participants ideally wanted to be able to
use the system to make direct, uncomplicated contact to
experts in the relevant field.


_**Close case**_
On closing a case, GPs would like to be able to enter confirmed
diagnoses into the system, as it would enable colleagues to
benefit and learn from their experience. The participants recommended that completed cases should be made available in
an edited form, so that other users could access them:

_When the case has been completed, then the possibil-_
_ity to describe it [would be useful], that is to say to see_
_the process, how the whole thing developed and what_
_actually came out of it all in the end. (WS, GP4)_


**Discussion**
Our requirements analysis was the first step in an UCD
process to develop a CDSS for primary care. With the
help of interviews and a workshop we identified user



needs and determined user requirements from the GP’s
perspective. The user requirements dealt with data entry,
presentation of results, discussion of results with colleagues and patients, the planning of further diagnostic
tests, referral to specialists, and case closure.


**Specific needs of general practice**
A CDSS to support diagnoses in the primary care sector
should fulfill specific requirements. Physicians criticized
alternative systems because they were designed with only
rare diseases in mind and did not take into account unusual symptom complexes and the common diseases that
play a major role in primary care. Additionally, many
such systems in Germany are currently only available for
a fee [40]. This may be a barrier, especially for small practices. Furthermore, once a differential diagnosis has been
provided, GPs wished for information on how to proceed,
such as diagnostic tests or indications to whom patients
could be referred. To the best of our knowledge, systems
that are available in Germany do not provide information
beyond diagnostic suggestions [41].


**Need for transparency**
Our results support the findings of other studies that GPs
expect a certain transparency when using AI [42, 43]. As
previous research has shown, GPs by no means want to
be replaced by AI and in some cases fear diminishing
capabilities if such systems regularly take over the ‘brainwork’ [14]. GPs are interested in suggestions, inspiration
and guidance, but ultimately want to choose and decide
themselves [41]. CDSS must address these needs by providing sources for the information they provide.


**Communication with colleagues and patients**
The results show that GPs would welcome the chance to
communicate with colleagues through the CDSS, which
the current software does not allow. In addition to the
passive decision support such a system provides, discussions with colleagues often provide important and
effective support when making a diagnosis [41]. The integration of a conversation option into the CDSS would
make the system significantly more attractive and effective. At the same time, the implementation of such an
option would require an extensive technical effort, which
may not be possible within the scope of SATURN.
Besides sharing information with colleagues, communication with patients also plays an important role. The
GPs discussed whether it would be useful to give patients
access to the system and permit them to enter data on,
for example, their symptoms themselves, and perhaps
to check the accuracy of their data. The literature also
emphasizes the importance of involving patients in their


Schütze _et al. BMC Medical Informatics and Decision Making     (2023) 23:144_ Page 8 of 10



own care through interactive tools [18]. However, no
consensus was reached on this topic in our workshop. We
therefore organized a workshop with patients to explore
their points of view, which will be described elsewhere.


**Interface to practice management system**
GPs said it was essential to be able to automatically
transfer patient data from electronic patient records to
the CDSS in order to save time and reduce transmission
errors. This requirement has also been mentioned in the
existing literature. Sutton et al., for example, argue that
CDSS can disrupt workflows if used as stand-alone systems and that poor system integration requiring manual
data entry is an important obstacle to the implementation of diagnostic decision support systems [18]. Nurek
et al. consider double entry of data as a barrier to the use
of CDSS and have therefore requested the integration
with electronic patient records [16]. This is a major problem in Germany, as many different providers of practice
management systems to manage patient records exist,
but mandatory data exchange standards do not [44–46].
Modern standards vary considerably, even though the
x-/BDT standard is widely used. However, an interface
to link to practice management systems is currently only
possible in cooperation with the companies themselves
and then only for particular applications. The aim of this
project is therefore to develop an initial strategy and to
discuss a preliminary solution with system providers.
A solution is, however, unlikely to be found in the near
term, if data loss is to be prevented [44, 46].


**UCD – benefits and challenges**
We consider it useful and feasible to involve GPs as
future users in the process. Despite their busy schedules, participants were highly motivated to take part in
the project. We believe that the prospect of a useful tool
that is specifically designed for their situation increased
their willingness to participate. Many ideas emerged on
what GPs would like to see in a CDSS. However, when
asking what an ‘ideal system’ would look like, it is challenging to prevent GPs from developing unrealistic
expectations. In addition to user requirements, technical feasibility and the scope of the project will have
to be taken into account during software development.
We will therefore prioritize user requirements regarding importance for the GPs and technical feasibility.
These prioritized user requirements will serve as a basis
in the development of mockups and, subsequently, the
first prototype. Hence, the next step is to translate user
requirements into system requirements and implement them technically. Mockups and prototypes will
be discussed and tested with participants in several
iterations.



**Strengths and limitations**
Studies with a small sample size are often viewed critically. In qualitative research and in UCD, however, it
is inherent in the method that an intensive exchange
takes place with a small group of participants. The goal
of qualitative methods is not to have a large, statistically
representative database but an in-depth examination of
individual cases that takes contexts and complexity into
account [47]. Especially in UCD, the continuous feedback
of participants is important in order to cooperate in shaping and developing the design [48]. In the workshop, the
group size of five made constructive discussion possible.
Moreover, our sample included both men and women
with different amounts of professional experience. In the
project, we will closely involve the participants in a number of iterations during system development. Additional
participants will be recruited for final usability testing.
The chosen methods (interviews and workshop) were
appropriate. By formulating needs and requirements
at the start of the UCD process, we ensured the users’
points of view were considered before taking the system’s
perspective. At the same time, it was sometimes difficult
to strictly adhere to the syntax rule and we occasionally
deviated from it slightly.
A particularly important step in the UCD was to provide participants with the opportunity to express their
ideas and needs in a workshop based on an open-ended
question. However, it was difficult to ask participants
what they would consider an ideal system to look like,
while at the same time communicating the limitations
inherent in the project.
Some specific results of the requirements analysis
may not be transferable to other countries due to differences in work processes. However, our methodological approach can be used and adapted by developers of
similar systems when available time and resources are
limited. Overall, a multidisciplinary study team proved
to be very helpful.


**Conclusions**
In order to develop a CDSS for diagnosis in primary
care, it proved useful to use interviews and a workshop
to conduct requirements analysis, as it enabled us to
gain an overview of workflows, information about the
user group, their tasks, and essential user requirements.
These findings can now be used to design mockups that
will be discussed with the users and then implemented
as a prototype.


**Abbreviations**
AI Artificial Intelligence
CDSS Clinical Decision Support System
GP General practitioner
UCD User-Centered Design


Schütze _et al. BMC Medical Informatics and Decision Making     (2023) 23:144_ Page 9 of 10



**Supplementary Information**

[The online version contains supplementary material available at https://​doi.​](https://doi.org/10.1186/s12911-023-02245-w)
[org/​10.​1186/​s12911-​023-​02245-w.](https://doi.org/10.1186/s12911-023-02245-w)


**Additional file 1.** Interview guide.

**Additional file 2.** User requirements list.

**Additional file 3.** Persona. The details in Addfile 3 are for the purposes of
illustration only and do not represent the data of any specific individual
involved in the study.


**Acknowledgements**
We would like to thank the physicians that participated in our study. We are
also grateful to Phillip Elliott for the language review of the paper.


**Authors’ contributions**
DS, SH, MN and SK collected, analyzed, and interpreted the data. JS, DS, LF, BS
and BSM contributed toward the conceptualization and methodology of the
study. JS and BSM applied for funding. DS, SH and SK drafted the manuscript,
which was critically revised by all authors. All authors read and approved the
final manuscript.


**Funding**
Open Access funding enabled and organized by Projekt DEAL. SATURN is
funded by the German Federal Ministry of Health as part of the research focus
"Digital Innovation", Module 3: "Smart Algorithms and Expert Systems" (grant
number: ZMI1-2520DAT02B).


**Availability of data and materials**
The datasets generated and/or analysed during the current study are not
publicly available due to the confidentiality promised to respondents at the
time of consent but are available from the corresponding author on reasonable request.


**Declarations**


**Ethics approval and consent to participate**
The ethics committee of Goethe University Frankfurt approved the study on
February 12, 2022 (ID: 2022–629). All participants provided written informed
consent to participate in the study. All methods were carried out in accordance with relevant guidelines and regulations.


**Consent for publication**
Not applicable.


**Competing interests**
The authors declare no competing interests.


**Author details**
1 Goethe University Frankfurt, Institute of General Practice, Theodor‑Stern‑Kai
7, 60590 Frankfurt, Germany. [2] Goethe University Frankfurt, University Hospital,
Institute of Medical Informatics, Frankfurt, Germany. [3] Executive Department
for Medical IT‑Systems and Digitalization, University Hospital Frankfurt, Goethe
University, Frankfurt, Germany. [4] Technische Universität Dresden, Institute
for Medical Informatics and Biometry, Carl Gustav Carus Faculty of Medicine,
Dresden, Germany. [5] University of Cologne, Faculty of Medicine and University
Hospital Cologne, Institute of General Practice, Cologne, Germany.


Received: 16 March 2023  Accepted: 19 July 2023


**References**
1. Singh H, Schiff GD, Graber ML, Onakpoya I, Thompson MJ. The global burden of diagnostic errors in primary care. BMJ Qual Saf. 2017;26:484–94.
[https://​doi.​org/​10.​1136/​bmjqs-​2016-​005401.](https://doi.org/10.1136/bmjqs-2016-005401)



2. Kostopoulou O, Delaney BC, Munro CW. Diagnostic difficulty and error in
[primary care–a systematic review. Fam Pract. 2008;25:400–13. https://​doi.​](https://doi.org/10.1093/fampra/cmn071)
[org/​10.​1093/​fampra/​cmn071.](https://doi.org/10.1093/fampra/cmn071)
3. Buzzetti E, Parikh PM, Gerussi A, Tsochatzis E. Gender differences in liver
disease and the drug-dose gender gap. Pharmacol Res. 2017;120:97–108.
[https://​doi.​org/​10.​1016/j.​phrs.​2017.​03.​014.](https://doi.org/10.1016/j.phrs.2017.03.014)
4. Guy J, Peters MG. Liver disease in women: the influence of gender on epidemiology, natural history, and patient outcomes. Gastroenterol Hepatol.
2013;9:633–9.
5. Pinkerton KE, Harbaugh M, Han MK, Le Jourdan Saux C, van Winkle LS,
Martin WJ, et al. Women and lung disease. sex differences and global
[health disparities. Am J Respir Crit Care Med. 2015;192:11–6. https://​doi.​](https://doi.org/10.1164/rccm.201409-1740PP)
[org/​10.​1164/​rccm.​201409-​1740PP.](https://doi.org/10.1164/rccm.201409-1740PP)
6. Silverman EK, Weiss ST, Drazen JM, Chapman HA, Carey V, Campbell EJ,
et al. Gender-related differences in severe, early-onset chronic obstructive
[pulmonary disease. Am J Respir Crit Care Med. 2000;162:2152–8. https://​](https://doi.org/10.1164/ajrccm.162.6.2003112)
[doi.​org/​10.​1164/​ajrccm.​162.6.​20031​12.](https://doi.org/10.1164/ajrccm.162.6.2003112)
7. Evans WR, Rafi I. Rare diseases in general practice: recognising the zebras
[among the horses. Br J Gen Pract. 2016;66:550–1. https://​doi.​org/​10.​3399/​](https://doi.org/10.3399/bjgp16X687625)
[bjgp1​6X687​625.](https://doi.org/10.3399/bjgp16X687625)
8. Haendel M, Vasilevsky N, Unni D, Bologa C, Harris N, Rehm H, et al. How
[many rare diseases are there? Nat Rev Drug Discov. 2020;19:77–8. https://​](https://doi.org/10.1038/d41573-019-00180-y)
[doi.​org/​10.​1038/​d41573-​019-​00180-y.](https://doi.org/10.1038/d41573-019-00180-y)
9. [European Commission. Rare Diseases. https://​resea​rch-​and-​innov​ation.​ec.​](https://research-and-innovation.ec.europa.eu/research-area/health/rare-diseases_en)
[europa.​eu/​resea​rch-​area/​health/​rare-​disea​ses_​en. Accessed 18 Jan 2023.](https://research-and-innovation.ec.europa.eu/research-area/health/rare-diseases_en)
10. Baynam G, Pachter N, McKenzie F, Townshend S, Slee J, Kiraly-Borri C, et al.
The rare and undiagnosed diseases diagnostic service - application of
massively parallel sequencing in a state-wide clinical service. Orphanet J
[Rare Dis. 2016;11:77. https://​doi.​org/​10.​1186/​s13023-​016-​0462-7.](https://doi.org/10.1186/s13023-016-0462-7)
11. Limb L, Nutt S, Sen A. Experiences of rare diseases: an insight from
patients and families. 2010.
12. Blöß S, Klemann C, Rother AK, Mehmecke S, Schumacher U, Mücke
U, et al. Diagnostic needs for rare diseases and shared prediagnostic
phenomena: Results of a German-wide expert Delphi survey. PLoS One.
[2017;12:e0172532. https://​doi.​org/​10.​1371/​journ​al.​pone.​01725​32.](https://doi.org/10.1371/journal.pone.0172532)
13. Gahl WA, Wise AL, Ashley EA. The undiagnosed diseases network of the
national institutes of health: a national extension. JAMA. 2015;314:1797–
[8. https://​doi.​org/​10.​1001/​jama.​2015.​12249.](https://doi.org/10.1001/jama.2015.12249)
14. Harada T, Miyagami T, Kunitomo K, Shimizu T. Clinical decision support
systems for diagnosis in primary care: a scoping review. Int J Environ Res
[Public Health. 2021. https://​doi.​org/​10.​3390/​ijerp​h1816​8435.](https://doi.org/10.3390/ijerph18168435)
15. Chima S, Reece JC, Milley K, Milton S, McIntosh JG, Emery JD. Decision
support tools to improve cancer diagnostic decision making in primary
[care: a systematic review. Br J Gen Pract. 2019;69:e809–18. https://​doi.​](https://doi.org/10.3399/bjgp19X706745)
[org/​10.​3399/​bjgp1​9X706​745.](https://doi.org/10.3399/bjgp19X706745)
16 Nurek M, Kostopoulou O, Delaney BC, Esmail A. Reducing diagnostic
errors in primary care. A systematic meta-review of computerized
diagnostic decision support systems by the LINNEAUS collaboration
on patient safety in primary care. Eur J Gen Pract. 2015;21(Suppl):8–13.
[https://​doi.​org/​10.​3109/​13814​788.​2015.​10431​23.](https://doi.org/10.3109/13814788.2015.1043123)
17. Sim I, Gorman P, Greenes RA, Hayney RB, Kaplan B, Lehmann H, Tang PC.
Clinical decision support systems for the practice of evidence-based
medicine. J Am Med Inform Assoc. 2001;8:527–35.
18. Sutton RT, Pincock D, Baumgart DC, Sadowski DC, Fedorak RN, Kroeker
KI. An overview of clinical decision support systems: benefits, risks, and
[strategies for success. NPJ Digit Med. 2020;3:17. https://​doi.​org/​10.​1038/​](https://doi.org/10.1038/s41746-020-0221-y)
[s41746-​020-​0221-y.](https://doi.org/10.1038/s41746-020-0221-y)
19. Chokshi SK, Belli HM, Troxel AB, Blecker S, Blaum C, Testa P, Mann D.
Designing for implementation: user-centered development and pilot
testing of a behavioral economic-inspired electronic health record clini[cal decision support module. Pilot Feasibility Stud. 2019;5:28. https://​doi.​](https://doi.org/10.1186/s40814-019-0403-z)
[org/​10.​1186/​s40814-​019-​0403-z.](https://doi.org/10.1186/s40814-019-0403-z)
20. Khairat S, Marc D, Crosby W, Al Sanousi A. Reasons for physicians not
adopting clinical decision support systems: critical analysis. JMIR Med
[Inform. 2018;6:e24. https://​doi.​org/​10.​2196/​medin​form.​8912.](https://doi.org/10.2196/medinform.8912)
21. Horsky J, Schiff GD, Johnston D, Mercincavage L, Bell D, Middleton B.
Interface design principles for usable decision support: a targeted review
of best practices for clinical prescribing interventions. J Biomed Inform.
[2012;45:1202–16. https://​doi.​org/​10.​1016/j.​jbi.​2012.​09.​002.](https://doi.org/10.1016/j.jbi.2012.09.002)


Schütze _et al. BMC Medical Informatics and Decision Making     (2023) 23:144_ Page 10 of 10



22. Schaaf J, Sedlmayr M, Schaefer J, Storf H. Diagnosis of Rare Diseases: a
scoping review of clinical decision support systems. Orphanet J Rare Dis.
[2020;15:263. https://​doi.​org/​10.​1186/​s13023-​020-​01536-z.](https://doi.org/10.1186/s13023-020-01536-z)
23. van Velsen L, Wentzel J, van Gemert-Pijnen JE. Designing eHealth that
Matters via a Multidisciplinary Requirements Development Approach.
[JMIR Res Protoc. 2013;2:e21. https://​doi.​org/​10.​2196/​respr​ot.​2547.](https://doi.org/10.2196/resprot.2547)
24. International Standards Organization. Ergonomics of Human-System
Interaction—Part 210: Human Centred Design for Interactive Systems,
ISO 9241–210. 2010.
25. LeRouge C, Wickramasinghe N. A review of user-centered design for
diabetes-related consumer health informatics technologies. J Diabetes Sci
[Technol. 2013;7:1039–56. https://​doi.​org/​10.​1177/​19322​96813​00700​429.](https://doi.org/10.1177/193229681300700429)
26. UXQB e.V. CPUX-F Curriculum and Glossary. 1st ed. 2020.
27. UXQB e.V. CPUX-UR Curriculum Certified Professional for Usability and
User Experience – User Requirements Engineering. 3rd ed. 2023.
28. Geis T, Tesch G. Basiswissen Usability und User Experience: Aus- und
Weiterbildung zum UXQB [®] Certified Professional for Usability and User
Experience (CPUX) - Foundation Level (CPUX-F). 1st ed. Heidelberg:
dpunkt.verlag; 2019.
29. Geis T. Praxiswissen User Requirements: Nutzungsqualität systematisch,
nachhaltig und agil in die Produktentwicklung integrieren: Aus- und
Weiterbildung zum UXQB Certified Professional for Usability and User
Experience - Advanced Level “User Requirements Engineering” (CPUXUR). 1st ed. Heidelberg: dpunkt.verlag; 2018.
30. Przyborski A, Wohlrab-Sahr M, editors. Qualitative Sozialforschung: De
Gruyter; 2021.
31. Unterauer M. Workshops im Requirements Engineering: Methoden,
Checklisten und Best Practices für die Ermittlung von Anforderungen. 1st
ed. Heidelberg: dpunkt-Verl; 2015.
32. Maguire M, Bevan N. User Requirements Analysis. In: Hammond J, Gross
T, Wesson J, editors. Usability. Boston, MA: Springer US; 2002. p. 133–148.
[https://​doi.​org/​10.​1007/​978-0-​387-​35610-5_9.](https://doi.org/10.1007/978-0-387-35610-5_9)
33. Tong A, Sainsbury P, Craig J. Consolidated criteria for reporting qualitative
research (COREQ): a 32-item checklist for interviews and focus groups.
[Int J Qual Health Care. 2007;19:349–57. https://​doi.​org/​10.​1093/​intqhc/​](https://doi.org/10.1093/intqhc/mzm042)
[mzm042.](https://doi.org/10.1093/intqhc/mzm042)
34. Palinkas LA, Horwitz SM, Green CA, Wisdom JP, Duan N, Hoagwood K.
Purposeful sampling for qualitative data collection and analysis in mixed
method implementation research. Adm Policy Ment Health. 2015;42:533–
[44. https://​doi.​org/​10.​1007/​s10488-​013-​0528-y.](https://doi.org/10.1007/s10488-013-0528-y)
[35. Nielsen J. Why You Only Need to Test With 5 Users. 2000. http://​www.​](http://www.useit.com/alertbox/20000319.html)

[useit.​com/​alert​box/​20000​319.​html. Accessed 6 Feb 2023.](http://www.useit.com/alertbox/20000319.html)
36. Nielsen J, Landauer TK. A mathematical model of the finding of usability
problems. In: Arnold B, van der Veer G, White T, editors. the SIGCHI conference; 24.04.1993 - 29.04.1993; Amsterdam, The Netherlands. New York,
[New York, USA: ACM Press; 1993. p. 206–213. https://​doi.​org/​10.​1145/​](https://doi.org/10.1145/169059.169166)
[169059.​169166.](https://doi.org/10.1145/169059.169166)
37. Baxter K, Courage C, Caine K. Understanding your users: A practical guide to
user research methods. Amsterdam, Netherlands: Morgan Kaufmann; 2015.
[38. Personas. https://​www.​usabi​lity.​gov/​how-​to-​and-​tools/​metho​ds/​perso​](https://www.usability.gov/how-to-and-tools/methods/personas.html)

[nas.​html. Accessed 3 Feb 2023.](https://www.usability.gov/how-to-and-tools/methods/personas.html)
39. Sunwar D, Stolworthy S. Proto-Persona: Define your target users. 2019.

[https://​openp​racti​celib​rary.​com/​pract​ice/​proto-​perso​na/. Accessed 14](https://openpracticelibrary.com/practice/proto-persona/)
Feb 2023.
40. Lenzen-Schulte M. Mit einem Mausklick zur Diagnose. Deutsches Ärzteblatt. 2017;114.
41 Müller T, Jerrentrup A, Schäfer JR. Computerunterstützte Diagnosefindung bei seltenen Erkrankungen. [Computer-assisted diagnosis of rare
[diseases]. Internist (Berl). 2018;59:391–400. https://​doi.​org/​10.​1007/​](https://doi.org/10.1007/s00108-017-0218-z)
[s00108-​017-​0218-z.](https://doi.org/10.1007/s00108-017-0218-z)
42. Schaaf J, Sedlmayr M, Sedlmayr B, Storf H. User-Centred development of
a diagnosis support system for rare diseases. Stud Health Technol Inform.
[2022;293:11–8. https://​doi.​org/​10.​3233/​SHTI2​20341.](https://doi.org/10.3233/SHTI220341)
43. Schaaf J, Sedlmayr M, Sedlmayr B, Prokosch H-U, Storf H. Evaluation
of a clinical decision support system for rare diseases: a qualitative
[study. BMC Med Inform Decis Mak. 2021;21:65. https://​doi.​org/​10.​1186/​](https://doi.org/10.1186/s12911-021-01435-8)
[s12911-​021-​01435-8.](https://doi.org/10.1186/s12911-021-01435-8)
44. Barkow L, Meincke O, Ulrich H, Ingenerf J. Fit for Purpose: Analyzing the
German Archiving and Exchange Interface for Medical Practice Manage[ment Systems. Stud Health Technol Inform. 2021;278:80–5. https://​doi.​](https://doi.org/10.3233/SHTI210054)
[org/​10.​3233/​SHTI2​10054.](https://doi.org/10.3233/SHTI210054)



45. Practice management systems (PVS). Installation statistics of software
[systems. https://​www.​kbv.​de/​html/​6989.​php. Accessed 3 Feb 2023.](https://www.kbv.de/html/6989.php)
46. Bertram O, Dorflinger S, Clin L, Polanc A, Koch R, Joos S, Thies C. Current
State of Interoperability in German Practice Management Systems:
Insights from the TeleDerm Project. In: 2018 IEEE 31st International
Symposium on Computer-Based Medical Systems (CBMS); 18.06.2018

[- 21.06.2018; Karlstad: IEEE; 2018. p. 217–222. https://​doi.​org/​10.​1109/​](https://doi.org/10.1109/CBMS.2018.00045)
[CBMS.​2018.​00045.](https://doi.org/10.1109/CBMS.2018.00045)
47. Witt H. Strategies in Qualitative and Quantitative Research. Forum Quali[tative Sozialforschung / Forum: Qualitative Social Research. 2001. https://​](https://doi.org/10.17169/fqs-2.1.969)
[doi.​org/​10.​17169/​fqs-2.​1.​969.](https://doi.org/10.17169/fqs-2.1.969)
48. Still B, Crane K. Fundamentals of User-Centered Design: CRC Press. 2017.


**Publisher’s Note**
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.










