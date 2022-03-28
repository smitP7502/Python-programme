# check armstrong number or not

num = 153
List = list(str(num))

sum = 0
for i in List:
    sum = sum +int(i)**3

if sum == num:
    print("number is palindrom")
else:
    print("not palindrom")