# practicequestion1 
age=12
if age < 13:
    print("You are a child.")
elif age< 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("senior citizen")

# practicequestion2

age=32
day="Monday"
if day=="wednesday":
    if age< 18:
        ticket_price=6
    else:
        ticket_price=10
else:
    if age< 18:
        ticket_price=8
    else:
        ticket_price=12
print("The ticket price is:",ticket_price)

# practicequestion3
score=85
match score:
    case 90|100:
        print("Grade A")
    case 80|89:
        print("Grade B")
    case 70|79:
        print("Grade C")
    case 60|69:
        print("Grade D")
    case _:
        print("Grade F")