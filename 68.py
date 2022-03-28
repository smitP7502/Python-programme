# print the letter except e and s

def Print(str):
    for i in str:
        if i.capitalize() not in ['E', 'S']:
            print(i, end="")


str = "Silver oak University"
Print(str)
