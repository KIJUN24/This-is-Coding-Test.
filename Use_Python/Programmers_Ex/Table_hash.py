def solution(data, col, row_begin, row_end):
    answer = 0
    s = 0
    s_list = []
    sum_list = []
    result = 0
    data.sort(key=lambda x:(x[col-1] ,-x[0]))
    for i in range(1, len(data)+1):
        for j in range(0, len(data[i-1])):
            s = data[i-1][j] % i
            s_list.append(s)
            if len(s_list) == 3:
                sum_list.append(sum(s_list))
                s_list = []
    
    result = sum_list[row_begin-1] ^ sum_list[row_end-1]
    print(result)

    return answer


solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3)