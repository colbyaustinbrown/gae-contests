n = int(input())

for i in range(0,n):
    name = input()
    vowels = 0
    for i in range(0,len(name)):
        print(name[i], end="")
        if name[i] in "aeiouAEIOU":
            vowels = vowels + 1
        if vowels == 2: break
    print("!")
        
