from os import getcwd
import sys
from hello_chai import chai,chai_one
from importlib import reload

print("Current working directory",getcwd())

for c in "chai":
    print(c, end="-")
print()

print("The platform is",sys.platform)

chai(69)
print(chai_one)
print(sys.getrefcount(69))

chai_types = {"masala": "spicy", "ginger": "zesty", "green": "mild"}

for key, value in chai_types.items():
    print(key,"=",value)

print("==================")
chai_types["milk"] = "milk"
del chai_types["green"]

for key, value in chai_types.items():
    print(key,"=",value)