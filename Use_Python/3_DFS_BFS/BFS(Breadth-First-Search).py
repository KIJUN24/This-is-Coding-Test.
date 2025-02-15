from collections import deque

# 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 라이브러리 사용
    queue = deque([start])
    # 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

visited = [False] * 9

bfs(graph,1 ,visited)