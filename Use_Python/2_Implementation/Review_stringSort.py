data = input()

result = []
value = 0

for i in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if i.isalpha():
        result.append(i)
    # 숫자는 따로 더하기
    else:
        value += int(i)
        print(value)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력
print(''.join(result))