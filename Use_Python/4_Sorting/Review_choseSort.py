array = [7,5,9,0,3,1,6,2,4,8]

# i : 가장 작은 데이터와 바뀔 인덱스, 매번 앞쪽으로 보내려고 하는 것것

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
            # print(min_index)

    # 스와프
    array[i], array[min_index] = array[min_index], array[i]
        
print(array)