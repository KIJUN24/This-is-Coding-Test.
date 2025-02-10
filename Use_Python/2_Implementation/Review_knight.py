input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a'))+1

to_move = [(-2,-1), (-2,1), (-1,2), (-1,-2), (1,2), (1,-2), (2,1), (2,-1)]

result = 0

for step in to_move:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)