def solution(r1, r2):
    count = 0
    y_min, y_max = r1, r2
    for x in range(0, r2):
        print(r2**2, y_max**2 + x**2)
        while r2**2 < y_max**2 + x**2:
            y_max -= 1

        while y_min-1 and r1**2 <= (y_min-1)**2 + x**2:
            y_min -=1

        count += y_max - y_min + 1

    # print(count*4)
    return count*4

solution(2, 3)