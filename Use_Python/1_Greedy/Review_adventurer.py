n = int(input())
scary = list(map(int, input().split()))

# 현재 그룹에 포함된 모험가의 수
count = 0
# 총 그룹의 수수
result = 0

scary.sort()

# print(scary)

# 공포도를 낮은 것부터 하나씩 확인
for i in scary:
    # 현재 그룹에 해당하는 모험가를 포함시키기
    count += 1
    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    if count >= i:
        # 총 그룹의 수 증가
        result += 1
        # 현재 그룹에 포함된 모험가 수 초기화
        count = 0

print(result)