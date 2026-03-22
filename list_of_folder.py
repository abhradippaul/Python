import os
from class_obj import test_func
from class_obj import Car
# folder_path = input("Enter the folder path: ")

try:
    folder_path = "../Youtube/Backend"

    contents = os.listdir(folder_path)

    for item in contents:
            print(item, "and the size is", os.path.getsize(os.path.join(folder_path, item)) / 1024, "KB")
    
except Exception as e:
    print(f"Error occurred while processing: {e}")

test_func("Abhradip Paul")

my_bmw = Car("BMW", "m5")

my_bmw.display_fullname()

print(isinstance(my_bmw, Car))  # True