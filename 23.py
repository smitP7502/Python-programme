# make even number of tuple

t1 = (1,2,3,4,5,6,7,8,8,9,10)
l = [i for i in t1 if i%2 == 0]
t2 = tuple(l)
print(t2)