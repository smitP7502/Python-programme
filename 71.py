# find the occrunces from the string for particular character
def Count(str, ch):
    count = 0
    for i in str:
        if ch == i:
            count += 1

    return count

str = "Hello! Friends chai piillo!!!"

Char = input("Enter the character which you have to find it's occurnces : ")
count = Count(str, Char)
print(f"The number of occrunces is : {count}")