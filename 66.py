# make simple computer

print("Enter the two numbers : ")
num1 = int(input("num1 : "))
num2 = int(input("num2 : "))

print("Enter the \n1-addition\n2-subtraction\n3-multiplication\n4-division : ")
op = int(input())

if op == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == 2:
    print(f"{num1} / {num2} = {num1 / num2}")

