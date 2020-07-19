# taking input from user for all subjects 

math_input = int(input("Enter marks aquired in Mathametics: "))
science_input = int((input("Enter marks aquired in Science: ")))
english_input = int(input("Enter marks aquired in English: "))
sports_input = int(input("Enter marks aquired in Sports: "))
computer_input = int(input("Enter marks aquired in Computer: "))

grade = (math_input + science_input + english_input + sports_input + computer_input)/5

if grade >= 90:
    print("You have obtained A grade") 
elif grade < 90 and grade > 70:
    print("You have obtained B grade")
elif grade < 70 and grade >50:
    print("You have obtained C grade")
elif grade < 50 and grade >30:
    print("You have obtained D grade")
elif grade < 30:
    print("You have obtained E grade")
else:
    print("You have entered Invalid Text")
