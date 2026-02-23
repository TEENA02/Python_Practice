import time
def cache_result(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Returning cached result for arguments:", args)
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            print("Calculating and caching result for arguments:", args)
            return result
    return wrapper
@cache_result
def func_runner_time(a,b):
    time.sleep(2)
    return a+b

print(func_runner_time(2,3))
print(func_runner_time(4,5))
print(func_runner_time(2,3))    



