# Sliver 3
# 징검다리


# 처음 아이디어 -> dp 인가? -> 밟을 징검다리(n-1번, n-2번 ... ) 너무 많음, 규칙 찾을 수 없음
# 밟을 수 있는 징검다리의 최대 수를 구할 수 있는 방법: 1부터 계속 더해서 주어진 수 n이 되기 직전 또는 넘어간 후 또는 딱 n일 때의 수를 찾아야한다.
# 주어진 수 100을 예시로 들면, 이분탐색시 1+2+...+13 = 91 100을 넘어가기 직전 13를 찾게된다.
# 그 다음 수 14를 더하면 105가 나오는데, 주어진 수 100을 구하려면 숫자 5를 빼면 된다.
# 근데 14를 더하고, 5를 뺀 것이기때문에 최대 징검다리의 개수는 동일하다.
# 주어진 수 1000000 같은 경우, 1+2+...+1414 = 1000405 주어진 수를 넘어간 후 1414를 찾게 된다.
# 그럴 경우는 숫자 405 1개를 빼면 되므로 1414-1 = 1413을 리턴해준다.

def binarySearch(rocksNum):  # 이분탐색
    start = 0
    end = rocksNum

    while start <= end:
        mid = (start + end) // 2
        sumValue = mid * (mid + 1) // 2  # 가우스의 덧셈; 1~n번까지의 합

        if sumValue > rocksNum:
            end = mid - 1
        else:
            start = mid + 1

    if sumValue <= rocksNum:
        return mid
    else:
        return mid - 1


maxRocks = []
t = int(input())
for i in range(t):
    rocksNum = int(input())
    maxRocks.append(binarySearch(rocksNum))

for rock in maxRocks:
    print(rock)

