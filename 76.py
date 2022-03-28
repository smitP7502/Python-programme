# count the wovels from the string

def Count_wovels(str):
    count = 0
    wovels = ['a','e','i','o','u']
    for i in str:
        if i in wovels:
            count += 1

    return count

str = "Hello! What are you doing?"
count = Count_wovels(str)
print(f"The number of wovels in the string is {count}")