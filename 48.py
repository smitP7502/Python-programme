# convert decimal to binary

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end="")

num = 11
DecimalToBinary(num)
