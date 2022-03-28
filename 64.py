# remove common elements from the two list

List1 = [1,2,3,4,5]
List2 = [3,4,5,6,7,8]

s1 = set(List1)
s2 = set(List2)

L1 = list((s1.union(s2)).difference(s1.intersection(s2)))

print(L1)