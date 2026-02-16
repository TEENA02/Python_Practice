username="teena sajwan"
def print_username():
    # username="teena"
    print(username)
print(username)
print_username()

x=100
# def print_x():
#     global x
#     x=1001

# print(x)
# print_x()
# print(x)
# def fun1():
#     # x=22
#     def f2():
#         print(x)
#     f2()
# fun1()
def fun1():
    # x=22
    def f2():
        print(x)
    return f2
res= fun1()
res()

def code1(vr):
    def code2(y):
        return y**vr
    return code2
square= code1(2)
cube= code1(3)
print(square(5))
print(cube(5))
# closure is a function object that remembers values in enclosing scopes 
# even if they are not present in memory.