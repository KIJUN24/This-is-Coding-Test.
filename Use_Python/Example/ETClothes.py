def solution(n, lost, reserve):
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)

    print(reserve_only, lost_only)

    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)

    print(n-len(lost_only))

    return n - len(lost_only)

solution(5, [2,4], [1,3,5])