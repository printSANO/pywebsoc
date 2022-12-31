import requests
import random
from bs4 import BeautifulSoup as bs

def getYear() -> str:
    """Check for the newly updated course term.

    Args:
        None
    Returns:
        Current year and term

    """
    base_url = "https://www.reg.uci.edu/perl/WebSoc"
    headers = {"User-Agent": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.{random.randrange(99)} (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"}
    
    response = requests.post(base_url, headers=headers)
    soup = bs(response.text, features="html.parser")
    r1 = soup.find('select').findChildren()
    result = ""
    for i in r1:
        text = i.string
        if "(Law)" not in text:
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
    elif "Summer" in result and "10" in result:
        tag = "-39"
    elif "Summer" in result and "2" in result:
        tag = "-76"
    elif "Summer" in result and "1" in result and "Session" in result:
        tag = "-25"
    return f"{year}{tag}"
