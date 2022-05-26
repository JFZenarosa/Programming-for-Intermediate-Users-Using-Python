#Coding Exercise 1.9
class ClubMembers:
    def __init__(self, name, birthday, age, favoriteFood, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favoriteFood = favoriteFood
        self.goal = goal
    
    def display1(self):
        print("parent information:")
        print("name: " + self.name)
        print("Birthdate: " + self.birthday)
        print("Age: " + str(self.age))
        print("Favorite food: " + self.favoriteFood)
        print("Goal: " + self.goal)

class ClubOfficers(ClubMembers):

    def __init__(self, name, birthday, age, favoriteFood, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favoriteFood, goal)
    
    def display2(self):
        print("child information:")
        print("name: " + self.name)
        print("Birthdate: " + self.birthday)
        print("Age: " + str(self.age))
        print("Favorite food: " + self.favoriteFood)
        print("Goal: " + self.goal)
        print("Position: " + self.position)
        
m_1 = ClubMembers("Tom", "January 16", 14, "Ice cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

m_1.display1()
print()
o_4.display2()