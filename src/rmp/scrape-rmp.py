import requests
from bs4 import BeautifulSoup
import json


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/75.0.3770.142 Safari/537.36"
}

def format_proff(raw_name):
    return "%20".join(raw_name)

def shovel(raw_proff):
    fixed_name = raw_proff.split(".")
    
    proff_query = format_proff(fixed_name)
    query_url = f'https://www.ratemyprofessors.com/search.jsp?queryoption=HEADER&queryBy=teacherName&schoolName=University+of+California+Irvine&sid=1074&query={proff_query}'
    page = requests.get(url=query_url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    scr = str(soup.find_all('script')[10])
    data = scr[scr.index("window.__RELAY_STORE__ = ") + len("window.__RELAY_STORE__ = "):scr.index("}};") + 3].replace("\\", "")
    json_data = json.loads('{"data":{' + data[data.index("legacyId") - 1:data.index("UC Irvine") + 10] + "}" + "}")
    del json_data['data']['school']#, json_data['U2Nob29sLTEwNzQ=']

    json_data['data']['proff_ID'] = json_data['data']['legacyId']

    del json_data['data']['legacyId']
    print(json_data)

    return json_data

def gen_link(proff_info):

    data = shovel(proff_info)
    
    proff_url = f"https://www.ratemyprofessors.com/professor?tid={data['data']['proff_ID']}"



if __name__ == "__main__":
    gen_link("A.KRONE-MARTINS")