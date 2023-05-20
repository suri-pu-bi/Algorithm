# Gold 5
# CCW

# 점 p1, p2를 지나가는 직선 그래프
# 그래프 위쪽 모든 영역에 있는 p3는 어느점이든 반시계방향이고,
# 그래프 아래쪽 모든 영역에 있는 p3는 어느점이든 시계방향이다.
# 위쪽 점 p3은 삼각형을 만들었을 때 높이가 + 이고,
# 아래쪽 점 p3은 삼각형을 만들었을 때 높이가 - 이므로
# 세 점의 좌표를 알 때, 삼각형의 넓이 신발끈 공식 이용하여
# 방향성을 구할 수 있다.
# S = 1/2 |x1y2 + x2y3 + x3y1 - x2y1 - x3y2 - x1y3 |



import sys

# 삼각형 공식
def ccw(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1]))

box = []
for i in range(3):
    box.append(tuple(map(int,sys.stdin.readline().split())))

result = ccw(box[0], box[1], box[2])

if result < 0:
    print(-1)
elif result > 0:
    print(1)
else:
    print(0)


