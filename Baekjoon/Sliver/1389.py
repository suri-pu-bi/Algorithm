# Sliver 1
# 케빈 베이컨의 6단계 법칙

from collections import deque


def dfs(graph, start):
    queue = deque()
    visited = [0] * (n + 1)
    queue.append(start)
    visited[start] = 1

    while queue:
        a = queue.popleft()

        for i in graph[a]:
            if not visited[i]:
                visited[i] = visited[a] + 1  # 중요 포인트; 시작 노드에서 연결된 노드까지 단계 수 누적해서 넣기
                queue.append(i)

    return sum(visited)


n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]  # 노드 번호 1부터 시작
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 노드 그래프

result = []
for i in range(1, n + 1):
    result.append(dfs(graph, i))

print(result.index(min(result)) + 1)  # 1부터 시작하므로 1 더하기
