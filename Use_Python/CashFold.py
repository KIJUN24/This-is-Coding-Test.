answer = 0
def solution(wallet, bill):
    global answer
    
    if wallet[0] < bill[0]:
        bill[0] //= 2
        answer += 1
        solution(wallet, bill)
    if wallet[1] < bill[1]:
        bill[1] //= 2
        answer += 1
        solution(wallet, bill)

    # print(answer)

    return answer



solution([50, 50], [100, 241])

# 50 241     50 120      50 60     50 30         