# Sliver 1
# 신입사원

import sys
t = int(sys.stdin.readline())


for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 1

    scores = [0] * (n + 1) # 왼쪽 성적은 어쩌파 정렬 -> 인덱스처럼 받을 리스트 설정
    for _ in range(n):
        a,b = map(int,sys.stdin.readline().split())
        scores[a] = [b]

    minValue = scores[1] # 첫번째 점수의 1등
    # 첫번째 서류 성적으로 정렬 -> 뒤의 지원자는 앞의 지원자보다 서류성적이 낮게 됨
    # 그럼 면접 성적만 비교하여 뒤의 지원자가 앞의 지원자의 min값보다 두번째 성적이 더 높다면 카운트 1추가
    for i in range(2,n+1):
        if scores[i] < minValue:
            minValue = scores[i]
            cnt += 1

    print(cnt)
