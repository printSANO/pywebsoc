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

    # Divison Options

    

def getEnrollInfo(year : str, code : str) -> dict:
    """Scrape enrollment info from webreg.

    Args:
        year: the year and term of class
        code: code of class
    Returns:
        A list of enrollment max, enrolled, waitlist, and requested.

    """
    base_url = "https://www.reg.uci.edu/perl/WebSoc"
    headers = {"User-Agent": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.{random.randrange(99)} (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"}
    params = {}
    params["YearTerm"] = year
    params["CourseCodes"] = code
    
    response = requests.get(base_url, params=params, headers=headers)
    print(response.text)
    # soup = bs(response.text, features="html.parser")
    # r1 = soup.find(valign='top', bgcolor='#FFFFCC').findChildren()

    # lst = []
    # for i in r1:
    #     lst.append(i.string)
    # data_dict = {}
    # b_index = lst.index("Bookstore")
    # data_dict["max_enroll"] = str(lst[b_index-5])
    # data_dict["enroll"] = str(lst[b_index-4])
    # data_dict["waitlist"] = str(lst[b_index-3])
    # data_dict["requested"] = str(lst[b_index-2])
    # return data_dict

# def checkSpace(jsondata: dict) -> bool:
#     """Check if space is available for enrollment.

#     Args:
#         lst: list of values from getEnrollmentInfo()
#     Returns:
#         A boolean with True is space is available and False else.

#     """
#     max_enroll = int(jsondata["max_enroll"])
#     enroll = int(jsondata["enroll"])
#     if max_enroll - enroll > 0:
#         return True
#     return False

def getYear() -> str:
    """Check for the newly updated course term.

    Args:
        None
    Returns:
        Current year and term

    """
    base_url = "https://www.reg.uci.edu/perl/WebSoc"
    headers = {"User-Agent": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.{random.randrange(99)} (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"}
    # params = {}
    # params["YearTerm"] = year
    # params["Breadth"] = "GE-1A"
    
    response = requests.post(base_url, headers=headers)
    soup = bs(response.text, features="html.parser")
    r1 = soup.find('select').findChildren()
    result = ""
    for i in r1:
        text = i.string
        if "(Law)" not in text:
            if "Summer" not in text:
                result = text
                break
    year = result[0:4]
    tag = ""
    if "Winter" in result:
        tag = "-03"
    elif "Fall" in result:
        tag = "-92"
    elif "Spring" in result:
        tag = "-14"
    return f"{year}{tag}"

if __name__ == "__main__":
    # y = getYear()
    # print(y)
    # x = getEnrollInfo(y, "35600")
    # print(x) #dict of data
    # b = checkSpace(x)
    # print(b) #bool
    webSocAPI()