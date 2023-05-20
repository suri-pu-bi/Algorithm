# Sliver 2
# 가장 긴 증가하는 부분 수열

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]

# 처음에는 이중 for문으로 처음부터 뒤 원소들까지 maxValue처리 -> 접근 방식이 잘못됨
# 1 2 3 101 4 5 6 일 경우
# maxValue가 101이 되고, 101과 그 뒤의 숫자를 비교하게 됨
# 첫 번째로 필요한 것: 어떻게 이어지게 할까?
# 현재 인덱스에 있는 값보다 그 전 인덱스에 있는 값들을 하나씩 비교해서 큰 경우에만 카운트
# 카운트 저장 필요, 미리 저장되어있던 값을 이어서 카운트하는 조건 필요 -> DP 이용

for i in range(n):
    for j in range(i):
        # dp[i] < dp[j]가 필요한 이유
        # 10 20 10 30 20 50이 주어졌을 때
        # 30인 경우, 10,20,10보다 다 크지만, 이어져있지 않으므로
        # 이 조건이 있어야 중간에 껴있는 10을 포함하는 일이 없어짐
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
            # print(dp)
    dp[i] += 1

print(max(dp))