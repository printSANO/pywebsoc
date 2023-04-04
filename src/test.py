from websocAPI import getYear, websocAPI, prettify

r = websocAPI(term=getYear(userTerm="Spring",userYear=2022),dept="I&C SCI", courseNum="33")
obj = prettify(r)
print(obj)