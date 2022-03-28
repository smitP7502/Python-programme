# swap last and first element of the list

List = ["smit", "het", "manan", "taxil", "aditya", "haresh"]
temp1 = List[0]
temp2 = List[len(List)-1]
L = []

List.remove(temp1)
List.remove(temp2)
List.append(temp1)
L.append(temp2)

new_List = L + List

print(new_List)