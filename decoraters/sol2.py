# def print_arguments(func):
#     def wrapper(*args, **kwargs):
#         print(f"Arguments passed to the function: {args}, {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper
# @print_arguments
# def print_return_value(a,b,*args):
#     return a+b

# print_return_value(2,4,9)
# my own solution
# custom solution
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments passed to the function: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value of the function: {result}")
        return result
    return wrapper
@debug
def greet(name,greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")