# Sliver 3
# 먹을 것인가 먹힐 것인가

def findResult(n, m, A, B):
    A.sort()
    B.sort()
    result = 0

    for i in range(n):
        start = 0
        end = m - 1
        while start <= end:
            mid = (start + end) // 2
            if B[mid] >= A[i]:
                end = mid - 1
            else:
                start = mid + 1
        result += (end + 1)

    return result


t = int(input())
result = []
for i in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result.append(findResult(n, m, A, B))

for i in result:
    print(i)