import sys
import heapq

input_value = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, iterable)
    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    result = result

n = int(input_value())
arr = []

for i in range(n):
    arr.append(int(input_value()))

res = heapsort(arr)

for i in range(n):
    print(res[i])