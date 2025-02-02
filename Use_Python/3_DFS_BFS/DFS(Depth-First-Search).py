# 함수 정의
def dfs(graph, v, visited):
    # 현재 노드 방문을 처리(방문했으면 Ture)
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 표현
graph = [
    [],             # 빈 노드(게산 하기 쉽게 0번은 비워둠.)
    [2, 3, 8],      # 1번 노드[1번 노드와 연결되어 있는 노드]
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현(현재 아무곳도 안 갔으니 False로 초기화)
visited = [False] * 9

# 함수 호출
dfs(graph, 1, visited)