# Bronze 2
# 탄산 음료

e,f,c = map(int, input().split())

cnt = 0
a = e+f
b = 0
while ((a+b)//c != 0):
  num1 = (a+b)//c
  num2 = (a+b)%c
  a = num1
  b = num2
  cnt += a
  print(a,b,cnt)
print(cnt)