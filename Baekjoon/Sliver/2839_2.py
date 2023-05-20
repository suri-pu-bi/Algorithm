# Sliver 4
# 설탕 배달 풀이 2


n = int(input())
cnt = 0
while n>=0:
  if n % 5 == 0:
    cnt += (n // 5)
    print(cnt)
    break # break문으로 나가면 else절은 실행되지 않는다
  n -= 3
  cnt += 1

else: # while문도 else절 존재 (조건식이 거짓이 판정되어서 while문이 수행되지 않을 때 else절이 수행됨)
  print(-1)