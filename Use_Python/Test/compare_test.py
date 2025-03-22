def solution(park, routes):

    move_tyep = {'E':(0,1), 'W':(0,-1), 'S':(1,0), 'N':(-1,0)}

    h,w = len(park), len(park[0])
    
    for r in range(h):
        for c in range(w):
            if park[r][c] == 'S':
                x,y = r,c
                break
    # print(x,y)
    
    for route in routes:
        direction, step = route.split()
        step = int(step)
        
        nx, ny = x,y
        
        for _ in range(step):
            nx += move_tyep[direction][0]
            ny += move_tyep[direction][1]
            
            if not (0 <= nx < h) and (0 <= ny < w):
                break
            
            if park[nx][ny] == 'X':
                break
                
        else:
            x,y = nx, ny        
    
    return [x,y]