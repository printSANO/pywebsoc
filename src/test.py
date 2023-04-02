from websocAPI import webscrape, utils

r = webscrape.webSocAPI(term=utils.getYear("Spring", 2023),dept="I&C SCI", courseNum="60", startTime="9:00am")
obj = utils.prettify(r)
print(obj)