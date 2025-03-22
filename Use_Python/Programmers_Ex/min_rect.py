def solution(sizes):
    answer = 0
    x_list = []
    y_list = []
    temp = 0

    for i in range(0, len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
        x_list.append(sizes[i][0])
        y_list.append(sizes[i][1])
    
    print(f"x_list:{x_list}   |   y_list:{y_list}")

    answer = max(x_list) * max(y_list)
    print(answer)
    return answer

solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])