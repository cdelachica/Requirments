your_name = input ("enter your name:")
name = ""
based_name = "Christian"

print("Your name should not have the same letter with Christan")

for letter in your_name:
 if letter not in based_name:
    name += letter
    print("\nAnalyzing letters at your name  :", name)

print("\nYour new name is :", name)


input("\nEnter to exit")