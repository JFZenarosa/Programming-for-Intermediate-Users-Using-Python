#Coding Exercise 2.4
flavors = ["vanilla", "chocolate", "strawberry", "cookies n' cream ", "bubblegum"]
toppings = ["almonds", "banana slices", "chocolate sycrup", "caramel syrup", "white chocolate chips"]
ice_cream = dict(zip(flavors, toppings))

print(ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update({"macha": "pistachios", "ube": "mango slices"})

print(ice_cream)