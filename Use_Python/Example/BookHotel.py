import heapq

def solution(book_time):
    def to_minutes(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    new_book_time = []  # 변환된 시간을 저장할 리스트

    for start, end in book_time:
        start_time = to_minutes(start)  # 시작 시간을 분으로 변환
        end_time = to_minutes(end) + 10  # 종료 시간 + 청소 시간(10분)

    new_book_time.append((start_time, end_time))  # 변환된 값을 리스트에 추가
    print(new_book_time)
    book_time.sort()

    rooms = []
    
    for start, end in book_time:
        if rooms and rooms[0] <= start:
            print(start)
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)


    print(len(rooms))

    return len(rooms)


solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])