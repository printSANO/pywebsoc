from websocAPI import webscrape, utils
import json


r = webscrape.webSocAPI(term=utils.getYear(),dept="I&C SCI", courseNum="33")
obj = json.dumps(r, indent=1)
print(obj)