cases = int(input())

for case_number in range(0,cases):

    [rows,cols] = list(map(int, input().split(" ")))
    maze = []
    flood = []

    start_r = 0
    start_c = 0
    end_r = 0
    end_c = 0
    
    for r in range(0,rows):
        line = input()
        maze.append(line)
        flood.append([0]*cols)
        for c in range(0, cols):
            if maze[r][c] == 'L':
                start_r = r
                start_c = c
            if maze[r][c] == 'E':
                end_r = r
                end_c = c

    flood[start_r][start_c] = 3
    cursteps = [(start_r,start_c)]

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while len(cursteps) > 0:
        nextsteps = []
        for (r0,c0) in cursteps:
            for i in range(0,4):
                r = r0 + dy[i]
                c = c0 + dx[i]
                if r < 0 or r >= rows or c < 0 or c >= cols: continue
                if maze[r][c] == '#': continue
                step = flood[r0][c0]
                if maze[r][c] == '!':
                    step = step - 1
                if flood[r][c] < step:
                    flood[r][c] = step
                    nextsteps.append((r,c))
        cursteps = nextsteps

    if flood[end_r][end_c] == 0:
        print("No solution")
    elif flood[end_r][end_c] == 1:
        print("1 heart")
    else:
        print(str(flood[end_r][end_c]) + " hearts")

