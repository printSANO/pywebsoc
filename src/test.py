from websocAPI import webscrape, utils
import json

r = webscrape.webSocAPI(term=utils.getYear("Spring", 2023),dept="I&C SCI", courseNum="60")
obj = json.dumps(r, indent=1)
print(obj)