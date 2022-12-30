import requests

def shovel():
    pass


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/75.0.3770.142 Safari/537.36"
}

url = "https://www.ratemyprofessors.com/search/teachers?query=thornton&sid=U2Nob29sLTEwNzQ="

test = requests.get(url)


#https://www.ratemyprofessors.com/ShowRatings.jsp?tid=2522809

testing = requests.get("https://www.ratemyprofessors.com/campusRatings.jsp?sid=1074")
#print(requests.get("https://www.ratemyprofessors.com/teachers.jsp?sid=1074").text)

url = "https://www.ratemyprofessors.com/search.jsp/teachers?sid=1074"


page = requests.get(url=url, headers=headers)
print(page.text)