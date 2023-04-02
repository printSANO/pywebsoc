from websocAPI import webscrape, utils

r = webscrape.webSocAPI(term=utils.getYear(userYear=2022),dept="I&C SCI", courseNum="33")
obj = utils.prettify(r)
print(obj)