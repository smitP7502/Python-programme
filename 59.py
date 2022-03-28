# number is prime or not

num = 37
c = 0

for i in range(2,num):
    if num % i == 0:
        c = 1
        break

if c == 1:
    print("Number is not prime number")
else:
    print("Number is prime number")