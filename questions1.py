# age = int(input("Enter your age: "))

# if age < 13:
#     print("You are Child")
# elif age < 20:
#     print("You are Teenager")
# elif age < 60:
#     print("You are Adult")
# else:
#     print("You are Senior")

# ===========================================

# from datetime import datetime
# age = int(input("Enter your age: "))

# ticket_price = 12

# if datetime.now().weekday() == 2:
#     ticket_price -= 2

# if age < 18:
#     ticket_price -= 4

# print("The ticket price is",ticket_price)

# ===========================================

# password = input("Enter your password: ")

# if len(password) >= 8:
#     if any(char.isdigit() for char in password):
#         print("Password is secure")
#     else:
#         print("Password is not secure")
# else:
#     print("Password length is too short")

# ===========================================

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# positive_count = 0

# for i in numbers:
#     if i > 0:
#         positive_count += 1

# print("The positive number count is",positive_count)

# ===========================================

# num = int(input("Enter a number: "))

# sum_result = 0

# for i in range(num+1):
#     if i % 2 == 0:
#         sum_result += i

# print("Sum of even number is",sum_result)

# ===========================================

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(10,"*",i,"=",10*i)

# ===========================================

# str = "Abhradip Paul"
# reverse_str = ""

# for char in str:
#     reverse_str = char + reverse_str
#     # print(str[len(str)-1-i])

# print("The reversed string is", reverse_str)

# ===========================================

# str = "Abhradip Paul"
# non_repeated_char = ""
# repeat_count = 0

# # for c in str.lower():
# #    if str.count(c) == 1:
# #       non_repeated_char = c
# #       break

# for c in str.lower():
#     for temp in str.lower():
#         if temp == c:
#             repeat_count += 1

#     if repeat_count == 1:
#         non_repeated_char = c
#         break
#     repeat_count = 0

# print("The first non repeated charater is", non_repeated_char)

# ===========================================

# num = int(input("Enter a number: "))

# result = 1

# while num > 1:
#     result *= num
#     num -= 1

# print("The factorial is:", result)

# ===========================================

num = int(input("Enter a number: "))
is_prime = True

for i in range(2,int(num/2)):
    if num % i == 0 and num > 1 :
        is_prime = False
        break

if is_prime:
    print(num, "is prime")
else:
    print(num, "is not prime")