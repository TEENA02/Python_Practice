import time
def time_func(func):
    def custome_func(*args,**kwargs):
       start=time.time()
       result = func(*args,**kwargs)
       end=time.time()
       print(f"Time taken to execute the {func.__name__} function: {end - start} seconds")
       return result
    return custome_func
@time_func
def calculate_sum(n):
    time.sleep(n)

calculate_sum(2)