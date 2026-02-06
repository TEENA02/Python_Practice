thisdisc={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdisc["model"])
print(thisdisc.get("brand"))
thisdisc['year']=2020
print(thisdisc)
# for x in thisdisc:
#     # print(x,end=" | ")
#     print(thisdisc[x],end=",")

for x,y in thisdisc.items():
    # print(x,end=" | ")
    print(x,y,end=",")
if "brand" in thisdisc:
    print("\nBrand is present in the dictionary")
thisdisc["color"]="red"
thisdisc["price"]=55000
print(thisdisc)
print(thisdisc.pop("brand")
)
print(thisdisc.popitem())
# Ford
# ('price', 55000)
del thisdisc["model"]
print(thisdisc)
cardetails=thisdisc.copy()
print(cardetails)

# dictionar in a dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },                       

    "child2" : {   
    "name" : "Tobias",
    "year" : 2007
  },
}
print(myfamily["child1"])
print(myfamily["child1"]["name"])

# keys in differnt list
keys=["brand","model","year"]
values=["Ford","Mustang",1964]
new_dict=dict.fromkeys(keys,values)
# {'brand': ['Ford', 'Mustang', 1964], 'model': ['Ford', 'Mustang', 1964], 'year': ['Ford', 'Mustang', 1964]}
