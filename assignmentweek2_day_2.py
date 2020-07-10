#calculator 
a1 = int(input("Enter first number: "))
a2 = int(input("Enter second number: "))
opr = input("Enter opr you need to use: ")

if opr == "+":
    print(f"sum of number is : {a1 + a2}")

elif opr == "-":
    print(f"differnece of number is : {a1 - a2}")

elif opr == "*":
    print(f"multiplication of two number is : {a1 * a2}") 

elif opr == "/":
    print(f"divison of two number is : {a1/a2}")

else:
    print("you entered the wrong input")