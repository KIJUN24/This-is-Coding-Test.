def solution(n):
    n_list = []
    first_idx = 0
    unclock_val = 0
    for i in range(10, -1, -1):
        a = n % pow(3, i)
        b = n // pow(3,i)
        if a < n:
            n = a

        n_list.append(b)
    # print(n_list)
    for idx, val in enumerate(n_list):
        if val != 0:
            first_idx = idx
            break
    
    n_list2 = n_list[first_idx:]
    n_list2.reverse()
    n_list3 = []

    for i in range(len(n_list2)-1, -1, -1):
        n_list3.append(n_list2[unclock_val] * pow(3, i))
        unclock_val += 1
    
    result = sum(n_list3)


    print(result)

solution(45)


# print(f"나머지 : {53 % pow(3,3)}")
# print(f"몫 : {53 // pow(3,3)}")

# print(f"나머지 : {26 % pow(3,2)}")
# print(f"몫 : {26 // pow(3,2)}")

# print(f"나머지 : {8 % pow(3,1)}")
# print(f"몫 : {8 // pow(3,1)}")

# print(f"나머지 : {2 % pow(3,0)}")
# print(f"몫 : {2 // pow(3,0)}")
