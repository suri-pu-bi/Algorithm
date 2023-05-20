# 실버 1
# 회의실 배정

import sys
n = int(sys.stdin.readline())
meeting = []
cnt = 1

for i in range(n):
    startTime, endTime = map(int, sys.stdin.readline().split())
    meeting.append((startTime, endTime))

# 끝나는 시간을 기준으로 정렬하면
# 작은 index값이 선택했을 때 cnt가 같거나 더 많을 수밖에 없다!
# -> Greedy
# key는 lambda와 함께 쓰인다!

# 같은 실수 반복
# 1, 2 / 2, 2: 종료시간이 같을 땐? 입력된 순서대로 하면 X
# 종료시간으로 정렬해서 같은 숫자가 나왔을 떄 시작시간도 순서대로 정렬해야함
meeting.sort(key=lambda x: (x[1], x[0]))

minValue = meeting[0][1]
for i in range(1,len(meeting)):
    if minValue <= meeting[i][0]:
        minValue = meeting[i][1]
        cnt += 1

print(cnt)