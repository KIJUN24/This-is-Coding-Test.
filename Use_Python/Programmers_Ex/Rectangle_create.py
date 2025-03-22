def solution(v):
    x = 0
    y = 0

    for i in range(3):
        x ^= v[i][0]
        y ^= v[i][1]

    print(x, y)

    return [x,y]

solution([[1,4], [3,4], [3,10]])