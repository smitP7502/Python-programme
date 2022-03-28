# sum of 1 to 5 using the recursion
def Add(num):
    if num == 1:
        return 1
    else:
        return num + Add(num - 1)


num = Add(5)
print("The sum of the 1 to 5 is : ", num)
