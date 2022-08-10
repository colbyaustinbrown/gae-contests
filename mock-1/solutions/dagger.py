n = int(input())

for i in range(0, n):
    line = list(map(int, input().split(" ")))
    rows = line[0]
    columns = line[1]
    time = line[2]


    maze = []
    flood = []
    start_r = -1
    start_c = -1
    for r in range(0, rows):
        maze.append(input())
        flood.append([-1]*columns)
        for c in range(0, columns):
            if maze[r][c] == 'S':
                flood[r][c] = 0
                start_r = r
                start_c = c

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    current_steps = [(start_r, start_c)]
    finished = False
    for t in range(0, time // 2):
        next_steps = []
        for (r,c) in current_steps:
            for i in range(0,4):
                nr = r + dy[i]
                nc = c + dx[i]
                if nr < 0 or nr >= rows or nc < 0 or nc >= columns:
                    continue
                if maze[nr][nc] == "#":
                    continue
                if maze[nr][nc] == "D":
                    finished = True
                    break
                if flood[nr][nc] == -1:
                    flood[nr][nc] = t + 1
                    next_steps.append((nr, nc))
            if finished: break
        if finished: break
        current_steps = next_steps
    if finished:
        print("Ofelia completes the task!")
    else:
        print("Ofelia can not complete the task.")

