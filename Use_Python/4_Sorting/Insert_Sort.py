array = [7,5,1,6,8,0,2,4,9,3]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        else:
            break
