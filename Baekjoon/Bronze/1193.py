# Bronze 1
# 분수 찾기
# 시간초과 해결 -> line별 개수 구하고, 그 개수의 합 구해서 x 번호가 있는 최종 line 구한 후 최종 line에 대하여 홀수 line/짝수 line 나눠서 최종번호까지 up, down 시키기

x = int(input())

up = 1
down = 1
line = 1
cnt = 0

while  cnt < x :
  cnt += line
  line += 1

line -= 1
cnt -= line

# print(cnt, line)

if line%2 == 0:
  down = line
  up = 1
  cnt += 1
  while (cnt < x):
    if cnt == x:
      break
    up += 1
    down -= 1
    cnt += 1

else:
  up = line
  down = 1
  cnt += 1
  while (cnt < x):
    if cnt == x:
      break
    up -= 1
    down += 1
    cnt += 1


print(str(up)+"/"+str(down))