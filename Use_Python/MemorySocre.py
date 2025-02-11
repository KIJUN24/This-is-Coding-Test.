name = list(map(str, input().split()))
yearning = list(map(int, input().split()))
photo = list(map(str, input().split()))

def solution(name, yearning, photo):
    answer = []
    answer_add = []
    for i in range(len(photo)):
        # print(photo[i])
        
        if len(photo[i]) < 3 or len(photo[i]) > 7:
            print("조건X")

        for j in range(len(name)):
            if len(name[j]) < 3 or len(name[j]) > 7:
                print("조건X")
            # print(yearning[j])

            if name[j] in photo[i]:
                # print(yearning[j])
                total_score = 0
                answer_add.append(yearning[j])
                total_score = sum(answer_add)
    answer.append(total_score)
    print(answer)

    return answer


solution(name, yearning, photo)