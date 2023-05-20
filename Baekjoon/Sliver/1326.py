# Sliver 2
# 폴짝폴짝

from collections import deque

def bfs(a, b, bridge, N):
    q = deque() # 큐 선언
    q.append(a-1) # 시작점 큐에 추가
    jump_check = [-1]*N # 방문을 안 했을 경우: -1, 방문을 했을 경우: 점프수 체크
    jump_check[a-1] = 0 # 시작점은 점프 수 0으로 초기화
    while q:
        node = q.popleft()
        for current in range(N): # 앞 뿐만 아니라 뒤로 가는 경우의 수도 생각해줘야함, 0~N-1번 반복하도록 설정
            # ex) 0이라는 노드에서 2이라는 숫자가 적혀있다고 가정한다. 그 뒤에 노드들을 하나씩 보는데,
            # 현재 보는 노드가 2라면, (2-0)%2 = 0 이므로 0노드에 적혀있는 수인 2의 배수만큼 이동한다는 조건 성립
            if (current-node)%bridge[node] == 0 and jump_check[current] == -1: # 방문하지 않았다면
                q.append(current) # 큐에 현재 노드 추가
                jump_check[current] = jump_check[node] + 1 # 현재 노드의 점프수를 1씩 추가
                # print(jump_check)
                if current == b-1: # 현재 위치와 도착점이 같다면
                    return jump_check[current] # 점프 수 리턴
    return -1 # b번 다리를 가지못했을 경우 -1 리턴

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b, bridge, N))