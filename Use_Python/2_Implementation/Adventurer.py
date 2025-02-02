people = int(input())
adventruer = list(map(int, input().split()))
adventruer.sort()
print(adventruer)

result = 0
count = 0

for i in adventruer:
    count += 1
    if count>= i:
        result += 1
        count = 0

print(result)