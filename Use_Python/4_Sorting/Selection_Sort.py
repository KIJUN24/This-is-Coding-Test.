array = [7,5,1,6,8,0,2,4,9,3]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    print(min_index) 
        
    array[i], array[min_index] = array[min_index], array[i]

# print(array)
