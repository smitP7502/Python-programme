# calculate the factorial of the number

def Fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*Fact(num-1)

num = int(input("Enter the number : "))
fact = Fact(num)
print("The factorial for the given number is ", fact)
