import requests
from bs4 import BeautifulSoup


url = "https://www.reg.uci.edu/perl/WebSoc"


payload = {
        "YearTerm": "2023-03",
    "Breadth": "ANY",
    "Dept": "ALL",
    "CourseNum": "",
    "Division": "ANY",
    "CourseCodes": "",
    "InstrName":"", 
    "CourseTitle": "",
    "ClassType": "ALL",
    "Units":"" ,
    "Days":"" ,
    "StartTime":"" ,
    "EndTime": "",
    "MaxCap": "",
    "FullCourses": "ANY",
    "FontSize": "100",
    "CancelledCourses": "Exclude",
    "Bldg": "",
    "Room": "",
    "Submit": "Display Web Results"
    }

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    
}

page = requests.get(url=url, headers=headers, data=payload)