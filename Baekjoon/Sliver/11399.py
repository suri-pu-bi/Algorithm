# Sliver 4
# ATM


def quick_sort1(array, start, end):
    if start >= end:
        return
    pivot = start  # 정렬되지 않았으므로 피벗을 첫 원소로 두기
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행

    quick_sort1(array, start, right - 1)
    quick_sort1(array, right + 1, end)


import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())
timeList = list(map(int, input().split()))
quick_sort1(timeList, 0, N - 1)

result = 0

for i in range(N):
    result += sum(timeList[:i + 1])

print(result)