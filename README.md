# **💡 pywebsoc**

> A python package for fetching data from the University of California, Irvine WebSoC (Schedule of Classes)
> Easily view courses and their details without needing to go into WebSoC

- Scrapes data from UCI WebSoC and returns a JSON data of courses.
- :warning: WARNING: Do not use this package any ways to exploit or harm UCI and its server.

## **Main Functions** ##
- The package consists of a main function, webSocAPI, in the webscrape module in the websocAPI package
- Some utils functions are inside utils module in the websocAPI package

### **Example Usages** ##

- How to start:

```python
from websocAPI import getYear, websocAPI
obj = webSocAPI(term=getYear("Spring", 2023),dept="I&C SCI", courseNum="193")
print(obj)
# {'I&C Sci 193 TUTORING IN ICS': [{'Code': '35990', 'Type': 'Lec', 'Sec': 'A', 'Units': '2', 'Instructor': 
# ['WONG-MA, J.', 'SHINDLER, M.'], 'Time': 'Tu \xa0  2:00- 3:20p', 'Place': 'ALP 1700', 'Final': 'Thu, Jun 15,
#  1:30-3:30pm', 'Max': '75', 'Enr': '0', 'WL': 'n/a', 'Req': '9', 'Rstr': 'B', 'Textbooks': 'Bookstore', 'Web': 
# None, 'Status': 'OPEN'}]}
```
- or you can also have a pretty json:
```python
from websocAPI import getYear, websocAPI, prettify
obj = webSocAPI(term=getYear("Spring", 2023),dept="I&C SCI", courseNum="193")
print(prettify(obj))
# {
#  "I&C Sci 193 TUTORING IN ICS": [
#   {
#    "Code": "35990",
#    "Type": "Lec",
#    "Sec": "A",
#    "Units": "2",
#    "Instructor": [
#     "WONG-MA, J.",
#     "SHINDLER, M."
#    ],
#    "Time": "Tu \u00a0  2:00- 3:20p",
#    "Place": "ALP 1700",
#    "Final": "Thu, Jun 15, 1:30-3:30pm",
#    "Max": "75",
#    "Enr": "0",
#    "WL": "n/a",
#    "Req": "9",
#    "Rstr": "B",
#    "Textbooks": "Bookstore",
#    "Web": null,
#    "Status": "OPEN"
#   }
#  ]
# }
```

### **Arguments and Parameters** ###

#### Function webSocAPI  ####

| webSocAPI's Parameters | Explanation |Default Value| Example Value|
| ------------- |:-------------:| :--------:| --------:|
| term          | Year and Term | ""        | "2023-14" |
| ge            | General education |  "ANY"   | "GE-2" |
| dept          | Department Name|   "ALL"    | "I&C SCI" |
| courseNum     | Course number or range     |    ""    | "193" |
| divison       | Course level      |   "ANY"    | "0xx" |
| secCodes      | Course code or range      |   ""   | "35870" |
| instrName     | Instructor      | ""    | "Doe, J." |
| courseTitle   | Course title contains...      | ""    | "GAME" |
| sectionType   | Course Type      |   "ALL"    | "LEC"  |
| units         | Units      | ""    | "4" |
| days          | Days     |  ""   | "TuTh" |
| startTime     | Starting time after|   ""   |  "9:00am"   | 
| endTime       | Ending time before      |  ""   | "9:00pm" |
| maxCap        | Maximum Capacity      |  ""  | ">50" |
| fullCourses   | Courses full option      |  "ANY"   |  "SkipFull" |
| cancelledCourses | Cancelled COurses     |  "EXCLUDE" | "Include" |
| building      | Building Code      |  ""   | "ELH" |
| room          | Class Room Number      |  ""  | "100" |

#### webSocAPI Parameters' Valid Values ####

##### term #####

| Valid Value | Explanation |
| ------------- |-------------|
| 2023-14        | 2023 is the year and 14 indicates Spring |
| 2023-03        | 2023 is the year and 76 indicates Winter |

- term can be autofilled using utils.getYear()
- Please check utils section

##### ge #####

| Valid Value | Explanation |
| ------------- |-------------|
| GE-1A        | Lower Divison Writing |
| GE-1B        | Upper Divison Writing |
| GE-2        | Science and Technology |
| GE-3        | Social and Behavioral Sciences |
| GE-4        | Arts and Humanities |
| GE-5        | Quantitative, Symbolic, and Computational Reasoning |
| GE-5A        | Quantitative Literacy  |
| GE-5B        | Formal Reasoning |
| GE-6        | Language Other Than English |
| GE-7        | Multicultural Studies |
| GE-8        | International/Global Issues |

##### dept #####

| Valid Value | Explanation |
| ------------- |-------------|
| AC ENG | Academic English |
| AFAM |   African American Studies |
| ANATOMY |  Anatomy and Neurobiology |
| ANESTH |    Anesthesiology |
| ANTHRO |    Anthropology |
| ARABIC | Arabic |
| ARMN |  Armenian (started 2018 Spg) |
| ART | Art |
| ART HIS | Art History |
| ARTS |   Arts |
| ARTSHUM |   Arts and Humanities |
| ASIANAM |   Asian American Studies |
| BANA |   Business Analytics (started 2017 SS2) |
| BATS |   Biomedical and Translational Science |
| BIO SCI | Biological Sciences |
| BIOCHEM |   Biological Chemistry |
| BME |    Biomedical Engineering |
| CAMPREC |  Campus Recreation |
| CBE |    Chemical and Biomolecular Engineering (started 2018 Fall) |
| CEM |    Community and Environmental Medicine |
| CHC/LAT |    Chicano Latino |
| CHEM |  Chemistry |
| CHINESE |   Chinese |
| CLASSIC |   Classics |
| CLT&amp;THY |   Culture &amp; Theory |
| COGS |   Cognitive Sciences  |
| COM LIT |    Comparative Literature |
| COMPSCI |   Computer Science |
| CRITISM |    Criticism |
| CRM/LAW |   Criminology, Law and Society |
| CSE |    Computer Science and Engineering |
| DANCE |  Dance |
| DATA |   Data Science (started 2022 SS1) |
| DERM |  Dermatology |
| DEV BIO |    Developmental and Cell Biology |
| DRAMA | Drama |
| EARTHSS |   Earth System Science |
| EAS |    East Asian Studies (started 2019 Fall) |
| ECO EVO |   Ecology and Evolutionary Biology |
| ECON |   Economics |
| ECPS |   Embedded and Cyber-Physical Systems |
| ED AFF | Educational Affairs (Sch of Med) |
| EDUC |   Education |
| EECS |   Electrical Engineering &amp; Computer Science |
| EHS |    Environmental Health Sciences |
| ENGLISH |   English |
| ENGR |   Engineering |
| ENGRCEE |  Engineering, Civil and Environmental |
| ENGRMAE |  Engineering, Mechanical and Aerospace |
| EPIDEM | Epidemiology |
| ER MED |    Emergency Medicine |
| EURO ST |   European Studies |
| FAM MED |   Family Medicine |
| FIN |  Finance (started 2017 Fall) |
| FLM&amp;MDA |  Film and Media Studies |
| FRENCH |    French |
| GDIM |   Game Design and Interactive Media (started 2021 Fall) |
| GEN&amp;SEX |   Gender and Sexuality Studies |
| GERMAN |   German |
| GLBL ME |   Global Middle East Studies |
| GLBLCLT |   Global Cultures |
| GREEK |  Greek |
| HEBREW |   Hebrew |
| HINDI |   Hindi |
| HISTORY |   History |
| HUMAN | Humanities |
| HUMARTS |   Humanities and Arts |
| I&C SCI |  Information and Computer Science |
| IN4MATX |    Informatics |
| INNO |   Masters of Innovation and Entrepreneurship (started 2019 Fall) |
| INT MED |    Internal Medicine |
| INTL ST |  International Studies |
| IRAN |   Iranian (started 2020 Fall) |
| ITALIAN | Italian |
| JAPANSE |   Japanese |
| KOREAN |   Korean |
| LATIN |   Latin |
| LAW |    Law |
| LIT JRN |  Literary Journalism |
| LPS | Logic and Philosophy of Science |
| LSCI |    Language Science (started 2019 Fall) |
| M&MG |  Microbiology and Molecular Genetics |
| MATH |   Mathematics |
| MED |    Medicine |
| MED ED |    Medical Education |
| MED HUM |   Medical Humanities |
| MGMT |  Management |
| MGMT EP |   Executive MBA |
| MGMT FE |   Fully Employed MBA |
| MGMT HC |   Health Care MBA |
| MGMTMBA |  Management MBA |
| MGMTPHD |  Management PhD |
| MIC BIO | Microbiology |
| MOL BIO |    Molecular Biology and Biochemistry |
| MPAC |  Accounting |
| MSE |    Materials Science and Engineering (started 2020 Fall) |
| MUSIC |  Music |
| NET SYS |   Networked Systems |
| NEURBIO |   Neurobiology and Behavior |
| NEUROL |    Neurology |
| NUR SCI |    Nursing Science |
| OB/GYN |    Obstetrics and Gynecology |
| OPHTHAL |   Ophthalmology |
| PATH |   Pathology and Laboratory Medicine |
| PED GEN |   Pediatrics Genetics |
| PEDS |   Pediatrics |
| PERSIAN |   Persian |
| PHARM | Pharmacology (started 2020 Fall) |
| PHILOS | Philosophy |
| PHMD |  Pharmacy (started 2021 Fall) |
| PHRMSCI |   Pharmaceutical Sciences |
| PHY SCI |    Physical Science |
| PHYSICS |   Physics |
| PHYSIO | Physiology and Biophysics |
| PLASTIC |    Plastic Surgery |
| PM&R |  Physical Medicine and Rehabilitation |
| POL SCI |    Political Science |
| PORTUG |    Portuguese |
| PSCI |   Psychological Science (started 2019 Fall) |
| PSYCH |  Cognitive Sciences |
| PUB POL |   Public Policy |
| PUBHLTH |   Public Health |
| RADIO |  Radiology |
| REL STD |    Religious Studies |
| ROTC |   Reserve Officers' Training Corps |
| RUSSIAN |   Russian |
| SOC SCI |    Social Science |
| SOCECOL |   Social Ecology |
| SOCIOL | Sociology |
| SPANISH |   Spanish |
| SPPS |   Social Policy & Public Service |
| STATS |  Statistics |
| SURGERY |  Surgery |
| SWE |   Software Engineering (started 2019 Fall) |
| TAGALOG |   Tagalog |
| TOX | Toxicology |
| UCDC |   UC Washington DC |
| UNI AFF | University Affairs |
| UNI STU | University Studies |
| UPPP |   Urban Planning and Public Policy (started 2018 Fall) |
| VIETMSE |   Vietnamese |
| VIS STD | Visual Studies |
| WRITING |    Writing |


##### courseNum #####

- Multiple entries allowed

| Valid Value | Explanation |
| ------------- |-------------|
| 5       | {dept} 5 equiavlent |
| 1-20       | {dept} 1 TO {dept} 20 equivalent |
| 5, 10       | {dept} 5 equiavlent AND {dept} 10 equivalent|

##### divison #####

| Valid Value | Explanation |
| ------------- |-------------|
| 0xx        | Lower Divsion Only |
| 1xx        | Upper Divsion Only |
| 2xx        | Graduate/Professional Only |

##### secCodes #####

| Valid Value | Explanation |
| ------------- |-------------|
| 35980       | Course Code 35980 |
| 35000-35600       | Courses with codes between 35000 and 36000 |

##### instrName #####

| Valid Value | Explanation |
| ------------- |-------------|
| Doe        | Last Name of Professors/TA |

##### courseTitle #####

| Valid Value | Explanation |
| ------------- |-------------|
| GAME       | Courses names that include GAME will be shown |

##### sectionType #####

| Valid Value | Explanation |
| ------------- |-------------|
| ACT        | Activity Courses |
| COL        | Colloquium Courses |
| DIS        | Discussion Courses |
| FLD        | Field Work Courses |
| LAB        | Laboratory Courses |
| LEC        | Lecture Courses |
| QIZ        | Quiz Courses |
| RES        | Research Courses |
| SEM        | Seminar Courses |
| STU        | Studio Courses |
| TUT        | Tutorial Courses |

##### units #####

| Valid Value | Explanation |
| ------------- |-------------|
| 4        | 4 Unit course, Any matching number is allowed |
| VAR        | Variable Unit course |

##### days #####

| Valid Value | Explanation |
| ------------- |-------------|
| MWF       | Includes Monday, Wednesday, Friday |
| MO       | Includes Monday |
| WE       | Includes Wednesday |
| FR       | Includes Friday |
| TuTh       | Includes Tuesday, Thursday |
| Tu       | Includes Tuesday |
| Th       | Includes Thursday |

##### startTime #####

| Valid Value | Explanation |
| ------------- |-------------|
| 9:00am        | classes that start at 9:00 AM or Later. Other times that follow the same format should work|
| 1:00pm       | classes that start at 1:00 PM or Later. Other times that follow the same format should wor |

##### endTime #####

| Valid Value | Explanation |
| ------------- |-------------|
| 1:00pm        | classes that end at 1:00 PM or Earlier |

##### maxCap #####

| Valid Value | Explanation |
| ------------- |-------------|
| >50        | Maximum capacity is atleast 50 |
| <100        | Maximum capacity is less than 100 |

##### fullCourses #####

| Valid Value | Explanation |
| ------------- |-------------|
| SkipFullWaitlist   | Skip any that are full unless Waitlist has space |
| SkipFull   | Skip any that are full |
| FullOnly   | Show only courses that are full or waitlisted |
| OverEnrolled   | Show only courses that are over-enrolled |

##### cancelledCourses #####

| Valid Value | Explanation |
| ------------- |-------------|
| EXCLUDE        | Default, Exclude cancelled courses |
| INCLUDE        | Include cancelled courses |
| ONLY        | Only show cancelled courses |

##### building #####

| Valid Value | Explanation |
| ------------- |-------------|
| ELH        | Engineering Lecture Hall Building Code |

- Please refer to UCI map for list of buildings and their codes

##### room #####

| Valid Value | Explanation |
| ------------- |-------------|
| 100        | {building} 100 equivalent classroom|

- Please refer to UCI map for list of buildings and their room numbers

#### Functions in Utils  ####

##### Function getYear #####

| Parameter | Exaplanation | Default Value | Example Value |
| ------------- | ------------- | ------------- | -------------|
| userTerm       | User customized term | None (not n/a)| Spring |
| userYear       | User customized year | None (not n/a)|  2022 |

- Examples of getYear function:

```python
from websocAPI import getYear
default_output = getYear() #This will return the most current year and term of courses available
manual_term = getYear("Winter") #This will return the Winter term of corresponding current year
manual_year = getYear(userYear=2021) ##This will return the most current term of 2021
manual_term_and_year = getYear("Winter", 2022) #This will return Winter term of 2022
```

##### Function prettify #####
| Parameter | Exaplanation | Default Value | Example Value |
| ------------- | ------------- | ------------- | -------------|
| obj       | Response from webSocAPI | n/a | data from webSocAPI |
| indents       | indent of prettified json | 1 |  2 |
