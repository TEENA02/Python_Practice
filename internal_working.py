a=[1,2,3]
b=a
print(a==b)
print(a is b)
b=[1,2,3]
print(a==b)
print(a is b)
# as in scalar variables, == checks for value equality while is checks for identity (same object in memory).