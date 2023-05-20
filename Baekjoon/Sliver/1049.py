# Sliver 4
# 기타줄

# 설계) 그리디 알고리즘 예상? 확인할 것! => 각 단계에서 최적의 결과를 선택했을 때 전체에서도 최적의 결과인가?
# 예제 입력/출력을 봤을 때 전체에서도 최적의 결과가 맞음

string_count, brand_count = map(int, input().split())
brand_info = []

for i in range(brand_count):
    strings6_price, string1_price = map(int, input().split())
    brand_info.append((strings6_price, string1_price))

# 기타줄 패키지의 가격 리스트 중 가장 작은 값 찾기
# 기타줄 낱개의 가격 리스트 중 가장 작은 값 찾기

minstrings6 = brand_info[0][0]
minstring1 = brand_info[0][1]

for i in range(1, brand_count):
    if minstrings6 > brand_info[i][0]:
        minstrings6 = brand_info[i][0]
    if minstring1 > brand_info[i][1]:
        minstring1 = brand_info[i][1]

# 끊어진 기타줄 개수 < 6
if string_count < 6:
    minValue = min(minstring1 * string_count, minstrings6)

# 끊어진 기타줄 개수 >= 6
else:
    use_package = string_count // 6
    # 기타줄 낱개 최솟값 * 끊어진 기타줄 개수와 기타줄 패키지 최솟값 * (끊어진 기타줄 개수 // 6 + 1) 둘 중 최솟값 구하기
    minValue = min(minstring1 * string_count, minstrings6 * (string_count // 6 + 1))

    while use_package != 0:
        # (끊어진 기타줄 개수 // 6) * 기타줄 패키지의 최솟값 + 기타줄 날개 최솟값  * (끊어진 기타줄 개수 - 6 * 끊어진 기타줄 개수 // 6)
        # (끊어진 기타줄 개수 // 6) - 1
        value = use_package * minstrings6 + minstring1 * (string_count - 6 * use_package)
        use_package -= 1
        # 구한 value가 minValue보다 작으면 minValue를 value로 바꿔주기
        if value < minValue:
            minValue = value

print(minValue)