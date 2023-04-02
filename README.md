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
from websocAPI import webscrape, utils
obj = webscrape.webSocAPI(term=utils.getYear("Spring", 2023),dept="I&C SCI", courseNum="193")
print(obj)
# {'I&C Sci 193 TUTORING IN ICS': [{'Code': '35990', 'Type': 'Lec', 'Sec': 'A', 'Units': '2', 'Instructor': 
# ['WONG-MA, J.', 'SHINDLER, M.'], 'Time': 'Tu \xa0  2:00- 3:20p', 'Place': 'ALP 1700', 'Final': 'Thu, Jun 15,
#  1:30-3:30pm', 'Max': '75', 'Enr': '0', 'WL': 'n/a', 'Req': '9', 'Rstr': 'B', 'Textbooks': 'Bookstore', 'Web': 
# None, 'Status': 'OPEN'}]}
```
- or you can also have a pretty json:
```python
from websocAPI import webscrape, utils
obj = webscrape.webSocAPI(term=utils.getYear("Spring", 2023),dept="I&C SCI", courseNum="193")
print(utils.prettify(obj))
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

### **Arguments and Parameters** ##

| WebSocAPI's Parameters | Explanation |Default Value   | Valid Values  |
| ------------- |:-------------:| :--------:| --------:|
| term          | year and term | ""        | 4 |
| ge            | centered      |   $12     | 4 |
| dept          | are neat      |    $1     | 4 |
| courseNum     | are neat      |    $1     | 4 |
| divison       | are neat      |    $1     | 4 |
| secCodes      | are neat      |    $1     | 4 |
| instrName     | are neat      |    $1     | 4 |
| courseTitle   | are neat      |    $1     | 4 |
| sectionType   | are neat      |    $1     | 4 |
| units         | are neat      |    $1     | 4 |
| days          | are neat      |    $1     | 4 |
| startTime     | are neat      |    $1     | 4 |
| endTime       | are neat      |    $1     | 4 |
| maxCap        | are neat      |    $1     | 4 |
| fullCourses   | are neat      |    $1     | 4 |
| cancelledCourses | are neat      |    $1  | 4 |
| building      | are neat      |    $1     | 4 |
| room          | are neat      |    $1     | 4 |


