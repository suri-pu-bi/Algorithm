# Bronze 3
# 택시 기하학


# 유클리드 기하학에서 두 지점의 거리는 좌표평면상의 최단거리
# 택시 기하학은 두 지점의 거리는 가로 세로로만 이동한 거리의 총합
# (대각선X 세로 가로 칸수로 따지면 이해쉬움)
# 택시 기하학에서 원은 마름모꼴
# 반지름의 길이에 따라 가로 2칸 세로 1칸 이런식으로 도형을 만들면 마름모꼴이 된다
# 택시 기하학에서의 원의 넓이 2*r*r

import math

r = int(input())
u_circle = math.pi * r * r
t_circle = 2 * r * r
print("{:.6f}".format(u_circle))
print("{:.6f}".format(t_circle))