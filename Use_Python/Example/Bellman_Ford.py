import sys

input_value = sys.stdin.readline
inf = (1e9)

# 노드의 개수, 간선의 개수 입력 받기
n,m = map(int, input_value().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
# 최단 거리 테이블을 무한으로 초기화
dist = [inf] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input_value().split())
    # a번 노드에서 b번 노드까지 가는데 걸리는 비용은 c이다
    edges.append((a, b, c))

def bf(start):
    # 시작 노드에 대하여 초기화
    dist[start] = 0
    # 전체 n번의 라운드(round)를 반복
    for i in range(n):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != inf and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
        
    return False

# 1번 노드가 시작 노드
negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for  i in range(2, n+1):
        # 도달할 수 없는 경우, -1 출력
        if dist[i] == inf:
            print("-1")
        else:
            print(dist[i])