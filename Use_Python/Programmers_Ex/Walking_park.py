def solution(park, routes):
    
    move = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}


    h,w = len(park), len(park[0])


    for r in range(h):
        for c in range(w):
            if park[r][c] == "S":
                x,y = r,c
                break
    
    
    for route in routes:
        direction, step = route.split()
        step = int(step)


        nx, ny = x, y
        for _ in range(step):
            nx += move[direction][0]
            ny += move[direction][1]


            if not (0 <= nx < h and 0 <= ny < w):
                break


            if park[nx][ny] == 'X':
                break
        else:

            x, y = nx, ny

    return [x,y]


solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]	)