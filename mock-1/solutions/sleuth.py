[r, c] = list(map(int, input().split(" ")))

puzzle = []
for y in range(0, r):
    puzzle.append(input())

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

n = int(input())
for i in range(0, n):
    word = input()
    for j in range(0, 8):
        for r2 in range(0, r):
            for c2 in range(0, c):
                y = r2
                x = c2
                found = True
                for char in word:
                    if x < 0 or x >= c or y < 0 or y >= r:
                        found = False
                        break
                    if puzzle[y][x] != char:
                        found = False
                        break
                    x = x + dx[j]
                    y = y + dy[j]
                if found:
                    print("{:d} {:d}".format(c2 + 1, r2 + 1))
                    break
            if found: break
        if found: break

