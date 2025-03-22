def solution(s):
    answer = []
    idx_char = {}

    for idx, char in enumerate(s):
        if char in idx_char:
            answer.append(idx - idx_char[char])
        else:
            answer.append(-1)
        idx_char[char] = idx
        print(idx_char[char])
    # print(answer)
    return answer

        
    
solution("banana")