import heapq

def solution(sequence, k):
    result = 0
    answer = []
    for i in range(len(sequence)):
        result += sequence[i]
        # print(result)
        if result == k:
            # print(result)

            answer.append(sequence.index(i))
            answer.append(sequence.index)
            break

    if result != k:
        heapq.heappop(sequence)
        solution(sequence, k)
        # print(sequence)

    print(answer)
    return answer

solution([1, 2, 3, 4, 5], 7)



