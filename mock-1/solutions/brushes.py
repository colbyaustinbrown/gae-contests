n = int(input())

for i in range(0, n):
    line = list(map(int, input().split(" ")))
    k = int(line[0])
    w = int(line[1])

    for j in range(0,k):
        x = int(line[2 + j])
        s = "#"*x
        print(("{:.^" + str(w) + "s}").format(s))

