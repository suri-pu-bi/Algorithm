# Sliver 1
# 숨바꼭질


import sys
from collections import deque

def bfs(v):
    q = deque([v]) # 큐 선언
    while q:
        v = q.popleft()
        if v == k: # 큐에서 꺼낸 노드가 k와 같을 때 (동생의 위치에 도착했을 때)
            return array[v] # 값 리턴
        for next_v in (v-1, v+1, 2*v): # -1만큼 이동, +1만큼 이동, *2만큼 순간이동할 수 있음
            if 0 <= next_v < MAX and not array[next_v]: # 범위 조건 and 방문하지 않았을 때
                # not array[i] -> array[i]가 0이면 실행
                array[next_v] = array[v] + 1 # 이동할 때마다 1초가 소요되므로 누적해서 시간 쌓기
                q.append(next_v) # queue에 이동한 위치 넣기



MAX = 100001 # 백준 범위
n, k = map(int,input().split())
array = [0] * MAX # 각 위치마다 몇 초 걸렸는지 담기 위한 리스트
print(bfs(n))
