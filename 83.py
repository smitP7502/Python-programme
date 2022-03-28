str = "Hello! My name is smit"

def Reverse(str):
    Str = list(str)
    Str.reverse()
    s = "".join(Str)
    return s

s = Reverse(str)
print(s)