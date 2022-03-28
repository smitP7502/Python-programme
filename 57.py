# sort list without built-in function

List = [12,31,321,3,231,90,1,32]
new_List = []

for i in range(len(List)):
    high = List[0]
    for j in List:
        if high > j:
            high = j


    List.remove(high)
    new_List.append(high)

print(new_List)