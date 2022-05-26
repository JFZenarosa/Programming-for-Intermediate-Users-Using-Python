#Coding Exercise 1.5
class Customers():
  greeting = "Welcome to Coffe Palace"
  def __init__(self, name, beverage, food, total):
    self.name = name
    self.beverage = beverage
    self.food = food
    self.total = total

c_1 = Customers("Nate", "Espresso", "Pastrani on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Iced tea", "Blueberry pancake", 315)

print(Customers.greeting)
print(c_2.name)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)
print(c_4.name)
print(c_4.beverage)
print(c_4.food)
print(c_4.total)
