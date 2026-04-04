f = open("./tea_list.py")

# print(f.readline())
# print(f.__next__()) # Give exception

# for i in f:
#     print(f.readline(), end="")

# while True:
#     line = f.readline()
#     print(line, end="")
#     if not line:
#         break

my_list = [1, 2, 3, 4]
i = iter(my_list)

print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())