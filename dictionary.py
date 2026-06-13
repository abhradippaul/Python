my_vehicle = {
    "model" : "Ford",
    "make" : "Explorer",
    "year" : "2018",
    "milage": 40000
}

for k, v in my_vehicle.items():
    print(f"Key is {k} and value is {v}")

vehicle2 = my_vehicle.copy()

vehicle2["number_of_tires"] = 4

del vehicle2["milage"]

print(vehicle2.keys())