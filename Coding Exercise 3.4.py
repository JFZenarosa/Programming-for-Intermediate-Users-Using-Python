#Coding Exercise 3.4
fileText = open("pythonEssay.txt", "w")
fileText.write("I like to learn in the future data science in python.")
fileText = open("pythonEssay.txt", "a")
fileText.write("\nMaking a project.")
fileText.write("\nDo coding challanges or building a python project.")
fileText.write("\nTo become a Python developer and data analyst in the future.")
fileText.close()