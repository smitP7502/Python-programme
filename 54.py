# find the sum of the digits for given number

num = 1234

List = list(str(num))

sum = 0
for i in List:
    sum = sum + int(i)

print(f"The sum of digit is {sum}")