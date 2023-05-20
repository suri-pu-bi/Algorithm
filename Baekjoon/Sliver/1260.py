# Sliver 2
# DFS와 BFS

from collections import deque


def dfs(graph, visited, v):
    visited[v] = 1
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, visited, i)


def bfs(graph, visited, v):
    visited[v] = 1
    queue = deque([v])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


n, m, v = map(int, input().split())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n + 1):
    graph[i].sort()

dfs(graph, visited, v)
visited = [0] * (n + 1)
print()
bfs(graph, visited, v)