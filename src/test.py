from websocAPI import webscrape, utils

r = webscrape.webSocAPI(term=utils.getYear("Spring", 2023),dept="I&C SCI", courseNum="193")
obj = utils.prettify(r)
print(obj)