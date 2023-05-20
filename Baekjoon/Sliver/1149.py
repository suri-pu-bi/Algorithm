# Sliver 1
# RGB 거리


import sys
n = int(sys.stdin.readline())
house = []
for _ in range(n):
    house.append(list(map(int,sys.stdin.readline().split())))


for i in range(1,n):
    # 현재집에서 빨간색을 선택했을 경우 전 집에서 초록색과 파란색 중 값이 작은 것을 선택해야함
    # 그리고 현재집의 값을 더해서 값 업데이트 해준다.
    house[i][0] = house[i][0] + min(house[i-1][1], house[i-1][2])
    house[i][1] = house[i][1] + min(house[i-1][0], house[i-1][2])
    house[i][2] = house[i][2] + min(house[i-1][0], house[i- 1][1])

# 맨 마지막 집에서 전체 결과의 값이 다 더해져서 나오기 때문에
# 마지막으로 빨간색,초록색,파란색 선택했을 때의 최솟값을 출력해준다
print(min(house[n-1][0], house[n-1][1], house[n-1][2]))