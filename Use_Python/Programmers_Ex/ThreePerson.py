def solution(number):
    answer = 0
    m_list = []
    z_list = []
    p_list = []
    
    number.sort()
    print(number)
    
    for i in range(0, len(number)):
        if number[i] < 0:
            m_list.append(number[i])
        elif number[i] == 0:
            z_list.append(number[i])
        else:
            p_list.append(number[i])

    print(m_list, z_list, p_list)

    return answer

solution([-2, 3, 0, 2, -5])