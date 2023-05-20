# Sliver 2
# 유기농 배추

from collections import deque


def bfs(graph, x, y):
    queue = deque()  # deque로 큐 선언
    graph[x][y] = 0  # 방문처리
    queue.append((x, y))  # 큐에 시작노드 추가

    # 2차원 리스트에서의 탐색위해 위치리스트 지정
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:  # 큐에 원소가 없을 때까지
        xpos, ypos = queue.popleft()  # 큐에서 노드꺼내기

        for i in range(4):  # 상하좌우 확인
            nx = xpos + dx[i]
            ny = ypos + dy[i]

            if 0 <= nx < m and 0 <= ny < n:  # 범위 지정 (Indexerror 생기지않게)
                if graph[nx][ny] == 1:  # 인접한 노드가 1이면
                    graph[nx][ny] = 0  # 방문 처리
                    queue.append((nx, ny))  # 큐에 인접한 노드 추가


t = int(input())
cnt_list = []

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for j in range(n)] for i in range(m)]  # 그래프 0으로 초기화
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1  # 배추가 심어져 있는 위치 => 1로 바꾸기

    # --- 그래프 구성

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:  # 그래프 하나씩 돌면서 1이면 (배추가 심어져있으면)
                bfs(graph, i, j)  # bfs 탐색
                count += 1  # bfs 탐색이 끝나면 모여있는 배추밭 1개가 탐색 완료되므로 배추흰지렁이의 개수 1개 추가

    cnt_list.append(count)

for cnt in cnt_list:
    print(cnt)