import requests
import random
from bs4 import BeautifulSoup as bs

def webSocAPI(term = "", ge = "ANY", dept = "ALL", courseNum = "", division = "ANY", secCodes = "", instrName = "", courseTitle = "", sectionType = "ALL", units = "", days = "", startTime = "", endTime = "", maxCap = "", fullCourses = "ANY", cancelledCourses = "EXCLUDE", building = "", room = ""):
    """Scrape info from webreg.

    Args:
        term: Class Term
        ge: General Education Category
        dept: Department Name
        courseNum: Course Number or Range ex. H2A, 5, 10-20
        division: Course Level
        secCodes: Course Code or Range ex. 14200, 29000-29100
        instrName: Name of Instructor ex. Smith
        courseTitle: Course Title Contains ex. Protein # Must have Instr, Course Code, Dept, or Breadth Specified
        sectionType: Course Type ex. Seminar # Must have Instr, Course Code, Dept, or Breadth Specified
        units: Units ex. 3, 4, or VAR # Must have Instr, Course Code, Dept, or Breadth Specified
        days: Days of Class ex. MWF, TuTh, W # Must have Instr, Course Code, Dept, or Breadth Specified
        startTime: Starting Time After # Must have Instr, Course Code, Dept, or Breadth Specified
        endTime: Ending Time Before # Must have Instr, Course Code, Dept, or Breadth Specified
        maxCap: Maximum Capacity ex. >50, <20 # Must have Instr, Course Code, Dept, or Breadth Specified
        fullCourses: Courses Full Option ex. Skip classes full # Must have Instr, Course Code, Dept, or Breadth Specified
        cancelledCourses: Cancelled Courses default-> Exclude Cancelled Courses 
        building: Building Code # Must have Instr, Course Code, Dept, or Breadth Specified
        room: Room Number # Must Building Specified

    Returns:
        A json response of collected info.
    """

    headers = {}
    parameters = {}
    # params = {}
    websoc = "https://www.reg.uci.edu/perl/WebSoc"

    headers["User-Agents"] = f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.{random.randrange(99)} (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
    parameters["ShowFinals"] = "1"
    parameters["ShowComments"] = "1"
    parameters["YearTerm"] = term
    parameters["Breadth"] = ge
    parameters["Dept"] = dept
    parameters["CourseNum"] = courseNum
    parameters["Divison"] = division
    parameters["CourseCodes"] = secCodes
    parameters["InstrName"] = instrName
    parameters["CourseTitle"] = courseTitle
    parameters["ClassType"] = sectionType
    parameters["Units"] = units
    parameters["Days"] = days
    parameters["StartTime"] = startTime
    parameters["EndTime"] = endTime
    parameters["MaxCap"] = maxCap
    parameters["FullCourses"] = fullCourses
    parameters["CancelledCourses"] = cancelledCourses
    parameters["Bldg"] = building
    parameters["Room"] = room
    response = requests.post(websoc, params=parameters, headers=headers)
    print(response.url)

# if __name__ == "__main__":
#     y = getYear()
#     print(y)
#     x = getEnrollInfo(y, "35600")
#     print(x) #dict of data
#     b = checkSpace(x)
#     print(b) #bool
#     webSocAPI(term=getYear(),secCodes="35600")