#Coding Exercise 2.8
groceries = {"chicken": 8, "apples": 6, "cucumbers": 3,"milk": 2, "oranges": 4}
remove = groceries.pop("oranges")
print(groceries)

speakers = {"Sir Rafael": 54, "Ms.Joan": 33, "Ms.Dana": 67}
speakerNames = speakers.keys()
print(speakerNames)

swimmingTeamTryOut = {"Carl": "Passed", "Quentin": "Failed", "John Y.": "Passed",
                      "Peter": "Failed", "Max T.": "Passed", "Joseph": "Passed",
                      "Jone": "Failed", "Jorge": "Failed", "George": "Passed",
                      "Ben": "Passed", "Jerome": "Passed", "Rick": "Failed",
                      "Max G.": "Failed", "John P.": "Failed", "Vince": "Passed"}
print(swimmingTeamTryOut["Jorge"])