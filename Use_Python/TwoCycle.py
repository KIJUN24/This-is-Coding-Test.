def solution(food):
    answer = ''

    # 정수형 리스트를 0 기준으로 좌우 대칭되게 배열 맞추기
    # food[0] = 물(한개)
    # food[i] = 정수형 배열 -> 홀수이면 하나 빼기
    # print(food[1])
    for i in range(1, len(food)):
        print(food[i])

    return answer

solution([1, 3, 4, 6])