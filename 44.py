# check triangle or not

print("Enter the length of three sides : ")
s1 = int(input("side 1 : "))
s2 = int(input("side 2 : "))
s3 = int(input("side 3 : "))

if s1 + s2 > s3 or s1 + s3 > s2 or s2 + s3 > s1:
    print("Triangle possible")
else:
    print("Triangle not possible")