num = int(input())
plans = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_type)):
        # print(plan)
        if plan == move_type[i]:
            nx  = x + dx[i]
            ny  = y + dy[i]
    if nx < 1 or ny < 1 or nx > num or ny > num:
        continue
    x, y = nx, ny

print(x, y)