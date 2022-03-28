# Print fibonachi serise

num = int(input("Enter the number : "))

n1 = 0
n2 = 1
next = 0
i = 0
print("Fibonachi serise : ")
while(i < num):
    print(n1)
    next = n1 + n2
    n1 = n2
    n2 = next
    i += 1

