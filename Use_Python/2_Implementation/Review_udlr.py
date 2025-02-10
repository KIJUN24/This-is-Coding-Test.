n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
move_types = ['R', 'U', 'L', 'D']

# r_move = [dx[0], dy[0]]
# u_move = [dx[1], dy[1]]
# l_move = [dx[2], dy[2]]
# d_move = [dx[3], dy[3]]

# 이동 계획 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동수행
    x, y = nx, ny

print(x,y)
