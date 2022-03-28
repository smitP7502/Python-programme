# find nth largest number from the list

List = [12,31,321,3,231,90,1,32]

List.sort()
num = int(input("Enter the number in the length of the list to find nth largest number : "))

print(f"{num}th largest element in the list is {List[num-1]}")