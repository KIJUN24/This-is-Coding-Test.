inf = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
n,m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [ [inf] * (n+1) for i in range(n+1)]
# 거쳐 갈 노드 x와 최종 목적지 노드 k를 입력받기
x,k = map(int, input().split())

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # a와 b가 서로에게 가는 비용은 1이라고 설정정
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1 출력
if distance >= inf:
    print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)