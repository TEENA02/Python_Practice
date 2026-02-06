thisdisc={
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdisc["model"])
print(thisdisc.get("brand"))
thisdisc['year']=2020
print(thisdisc)
for x in thisdisc:
    # print(x,end=" | ")
    print(thisdisc[x],end=",")
