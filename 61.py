# remove the multiple item from the list

def Remove(L, l):
    for i in l:
        if i in L:
            L.remove(i)

    return L

List = ["hello", "what", "where", "how", "which"]
remove = ["what", "how"]

print(Remove(List, remove))