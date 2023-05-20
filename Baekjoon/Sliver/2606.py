# Sliver 3
# 바이러스

def dfs(graph, node):
    visited = []
    stack = [node]
    cnt = 0

    while stack:
        x = stack.pop()
        visited.append(x)

        if graph[x]:
            for y in graph[x]:
                if y not in visited and y not in stack:
                    stack.append(y)
                    cnt += 1

    return cnt


n = int(input())
k = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(dfs(graph, 1))