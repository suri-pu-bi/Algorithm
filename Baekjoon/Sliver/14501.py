# 14501 퇴사 (실버 4)
# 저번과 같은 실수 반복: 그 다음것을 아예 선택해버리고 index를 이동하면,
# 그 다다음 것을 선택하는 게 최적의 결과일 수 있는데 무시됨.
# 동일한 작은 문제들이 반복하여 나타남 => DP 테이블 이용 (점화식 만들기!)

N = int(input())
counsel = []

for i in range(N):
  period, cost = map(int,input().split())
  counsel.append((period, cost))


value_list = [0 for _ in range(N+1)]
# 처음부터 하나씩 확인하는 for문 한개 필요
for i in range(N):
  # 하나 선택시 index 이동 후 그 나머지 값 하나씩 확인하는 for문 필요
  for j in range(i + counsel[i][0], N+1):
    # 리스트 갱신
    if value_list[j] < value_list[i] + counsel[i][1]:
      value_list[j] = value_list[i] + counsel[i][1]

# 리스트의 맨 끝값이 최댓값
print(value_list[-1])