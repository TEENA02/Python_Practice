# numbers is group of immutable data types , boolean is also included in this group , sets also partially immutable as its elements must be immutable
# immutable data types : int , float , complex , bool , string , tuple , frozenset
# mutable data types : list , set , dict
# immutable data types cannot be changed once created , any operation on immutable data types creates a new object in memory

a=10
b=7.8
print(a+b)
str="demo"
# print(str+9)
# TypeError: can only concatenate str (not "int") to str
# operater overloading is not supported between different immutable data types for example string and integer
# repr function returns a string representation of the object which can be used to recreate the object using eval function
repr('hello')  # "'hello'"
#x=str('hello')   # 'hello'
print('hello')  # hello
# floor and ceil and trunc functions are used to round off the float values
import math
print(math.floor(7.8))  # 7
print(math.ceil(7.2))   # 8
print(math.trunc(7.8))  # 7
print(math.trunc(-7.8)) # -7
# abs function returns the absolute value of a number
import random
print(random.random())
l1=[1,2,3,4,5]
print(random.choice(l1))  # randomly selects an element from the list
print(random.shuffle(l1))  # shuffles the list in place
print(l1)  # shuffled list