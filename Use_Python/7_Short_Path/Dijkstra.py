import sys

input_value = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input_value().split())
start = int(input_value())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [inf] * (n+1)

for _ in range(m):
    a, b, c = map(int, input_value().split())
    graph[a].append((b,c))


def get_smallest_node():
    min_value = inf
    index = 0

    for i in range(1,  n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijstra(start)

for i in range(1, n+1):
    if distance[i] == inf:
        print("infinity")
    else:
        print(distance[i])