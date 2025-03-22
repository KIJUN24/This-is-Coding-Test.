def solution(park, routes):
    # 방향에 따른 좌표 이동량 설정 (딕셔너리 사용)
    move = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}

    # 공원의 크기
    H, W = len(park), len(park[0])

    # 시작 위치(S) 찾기
    for r in range(H):
        for c in range(W):
            if park[r][c] == 'S':
                x, y = r, c  # 시작 위치 저장
                break

    # 명령어 수행
    for route in routes:
        direction, step = route.split()
        step = int(step)

        # 이동 가능 여부 확인
        nx, ny = x, y  # 현재 위치 저장
        for _ in range(step):
            nx += move[direction][0]
            ny += move[direction][1]

            # 공원 범위 밖이면 무시
            if not (0 <= nx < H and 0 <= ny < W):
                break

            # 장애물(X) 만나면 무시
            if park[nx][ny] == 'X':
                break
        else:
            # 모든 조건을 만족하면 이동
            x, y = nx, ny

    return [x, y]