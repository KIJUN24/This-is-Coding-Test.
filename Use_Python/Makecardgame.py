def solution(cards1, cards2, goal):
    answer = 'Yes'
    answer = ''

    result_arr1 = []
    result_arr2 = []
    result_arr = []
    sub_arr = []

    if len(cards1) <= 10 and len(cards2) <= 10:

        if cards1 != cards2:
        
            sub_arr.append(cards1[1])
            sub_arr.append(cards1[2])
            result_arr.append(cards1[0])
            for i in range(len(cards2)):
                result_arr.append(cards2[i])

            for i in range(len(sub_arr)):
                result_arr.append(cards1[i+1])

            if result_arr != goal:
                answer = 'No'
            else:
                answer = 'Yes'

        print(answer)

    # for i in goal:
    #     if i in cards1:
    #         result_arr1.append(cards1.index(i))
    #     elif i in cards2:
    #         result_arr2.append(cards2.index(i))

    # if not all(idx == cnt for idx, cnt in enumerate(result_arr1)) or not all(idx == cnt for idx, cnt in enumerate(result_arr2)):
    #     answer = "No"

    print(answer)

    return answer


solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])
# solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])