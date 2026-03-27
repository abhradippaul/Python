from random import choice,shuffle

tea_flavors = ["lemon", "masala", "ginger", "mint"]
print("Tea Flavors List:", tea_flavors)

# Creating a choice (picking a random flavor from the list)
selected_tea = choice(tea_flavors)
print("Selected Choice:", selected_tea)

# Shuffling the list
shuffle(tea_flavors)
print("Shuffled List:", tea_flavors)

