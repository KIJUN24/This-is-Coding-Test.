data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    # print(num)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
    
print(result)