# Sliver 3
# 친구

from collections import deque


def find(graph, target):
    visited = []
    visited_y = []
    queue = deque()
    queue.append((target, 0))
    cnt = 0

    while queue:
        x, depth = queue.popleft()
        visited.append(x)

        if depth == 2:
            return cnt

        for y in range(len(graph)):
            if graph[x][y] == 'Y':
                if y not in visited and y not in visited_y:
                    queue.append((y, depth + 1))
                    visited_y.append(y)
                    cnt += 1

    return cnt


n = int(input())
cnt_list = []

graph = [[j for j in input()] for i in range(n)]

for i in range(n):
    cnt = find(graph, i)
    cnt_list.append(cnt)

print(max(cnt_list))