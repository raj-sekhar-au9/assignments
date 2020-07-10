#Enter number to print a number pattern  
r = int(input("Enter any number: "))
for i in range(1, r+1):
    for c in range(1, i + 1):
        print(c, end=' ')
    print("")