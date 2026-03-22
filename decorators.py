import time


def timer(func):
    def wrapper(*args, **kwargs):
        joined_args = ", ".join(str(arg) for arg in args)
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Ther arguments are: ", joined_args)
        print(f"Execution name and time: {func.__name__} took {end - start} seconds")
        return result
    return wrapper

@timer
def example_function(n, m, x, y):
    time.sleep(n)
    print("This is an example function.")
example_function(2,6,10,45)

def test_function(*args):
    print("This is a test function that will be imported from another file", args)

test_function(1, 2, 3)