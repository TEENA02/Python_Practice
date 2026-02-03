tea=["balck tea","green tea","milk tea"]
print(tea)
print(tea[0:1])
tea.append("lemon tea")
print(tea)
tea.insert(2,"ginger tea")
print(tea)
tea[1:2]=['herbal tea']
print(tea)
tea[1:3]=['fruit tea','iced tea']

tea[1:1]=['non veg tea']
print(tea) # ['balck tea', 'non veg tea', 'herbal tea', 'fruit tea', 'iced tea', 'lemon tea']
for t in tea:
    print(t,end=" | ")
if "milk tea" in tea:
    print("\nmilk tea is present")


