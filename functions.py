# def square_of_num(num):
#     return num ** 2

# num = 3

# print(f"Square of num {num} is:", square_of_num(num))

# def multi(a, b):
#     return a * b

# print(multi(3, 7))
# print(multi("ab", 5))

# cube = lambda x: x ** 3

# print("The cube is", cube(3))

# def sum_all(*args):
#     print(args)
#     return sum(args)

# print(sum_all(1,2,3,4,5,6))

# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")

# print_kwargs(name="Abhradip Paul", age = "24")

def recursive(n):
    if n == 1:
        return 1
    return n * recursive(n - 1)

print(f"Factorial of 5 is {recursive(5)}")