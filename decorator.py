from time import time,sleep

# def timer(func):
#     def wrapper(*args, **kwargs):
#         print("The function arguments are", *args)
#         start = time()
#         print("Starting the function")
#         result = func(*args, **kwargs)
#         print("Ending the function")
#         end = time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper

# @timer
# def example_func(n):
#     sleep(n)

# example_func(2)

def cache(func):
    cache_values = {}
    def wrapper(*args):
        if args in cache_values:
            return cache_values[args]
        result = func(*args)
        cache_values[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    sleep(4)
    return a + b

print(long_running_function(2, 2))
print(long_running_function(2, 2))