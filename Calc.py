num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
action = str(input("Choose action: Add(a), Subtract(s), Multiply(m), Dividing(d)"))
if action == "a":
    print(num1+num2)
elif action == "s":
    print(num1-num2)
elif action == "m":
    print(num1*num2)
elif action == "d":
    print(num1/num2)
else:
    print("Please enter a number")

