def solutaion(clothes):
    # print(clothes)
    hash_map = {}
    for clothes_name, clothes_type  in clothes:
        # print(clothes_type, clothes_name)
        hash_map[clothes_type] = hash_map.get(clothes_type, 0) + 1
    
    answer = 1
    for i in hash_map:
        print(hash_map[i])
        answer *= (hash_map[i] + 1)

    print(answer-1)


solutaion([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])