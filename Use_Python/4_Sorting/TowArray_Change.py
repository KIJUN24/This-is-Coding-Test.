n,m = map(int, input().split())

array_1 = list(map(int, input().split()))
array_2 = list(map(int, input().split()))

array_1.sort()
array_2.sort(reverse=True)

for i in range(m):
    if array_1[i] < array_2[i]:
        array_1[i], array_2[i] = array_2[i], array_1[i]
    else:
        break

print(sum(array_1))