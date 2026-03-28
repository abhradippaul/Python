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

# num = int(input("Enter a number: "))
# is_prime = True

# if num > 1 :
#     for i in range(2,int(num/2)):
#         if num % i == 0 and num > 1 :
#             is_prime = False
#             break

# if is_prime:
#     print(num, "is prime")
# else:
#     print(num, "is not prime")

# ===========================================

# items = ["apple", "banana", "orange", "apple", "mango"]

# unique_set = set()

# for char in items:
#     if items.count(char) > 1:
#         print("The duplicate value is", char)
#         break

# for char in items:
#     if char in unique_set:
#         print("The duplicate value is", char)
#         break
#     unique_set.add(char)

# ===========================================

# from time import sleep,time_ns
# time = 1

# for i in range(5):
#     num = input("Enter a number: ")
#     print("Time stamp: ", time_ns())
#     print("Wait time: ", time)
#     sleep(time)
#     time *= 2


# from PIL import Image
# import piexif

# img = Image.new("RGB", (400, 300), color=(144, 144, 144))

# gps_ifd = {
#     piexif.GPSIFD.GPSLatitudeRef: b'N',
#     piexif.GPSIFD.GPSLatitude: [(37,1),(46,1),(30,1)],
#     piexif.GPSIFD.GPSLongitudeRef: b'E',
#     piexif.GPSIFD.GPSLongitude: [(122,1),(25,1),(10,1)],
# }

# exif_dict = {"GPS": gps_ifd}
# exif_bytes = piexif.dump(exif_dict)

# img.save("working_gps.jpg", "jpeg", exif=exif_bytes)

# from PIL import Image, ImageDraw
# import piexif

# img = Image.new("RGB", (400, 300), "white")
# draw = ImageDraw.Draw(img)

# # Add structure (important for hashing)
# draw.rectangle([50, 50, 350, 250], outline="black", width=5)
# draw.line((0, 0, 400, 300), fill="black", width=3)

# gps_ifd = {
#     piexif.GPSIFD.GPSLatitudeRef: b'N',
#     piexif.GPSIFD.GPSLatitude: [(37, 1), (45, 1), (33314, 1000)],  # 37°45'33.314"
    
#     piexif.GPSIFD.GPSLongitudeRef: b'W',
#     piexif.GPSIFD.GPSLongitude: [(122, 1), (29, 1), (12426, 1000)],  # 122°29'12.426"
# }

# exif_dict = {"GPS": gps_ifd}
# img.save("better_test.jpg", exif=piexif.dump(exif_dict))