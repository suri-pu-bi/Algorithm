# Bronze 2
# 알파벳 거리

# 알파벳을 숫자로 만들고 싶을때 아스키코드 이용하기!

N = int(input())
for i in range(N):
  testcase = input().split()
  d_list = []
  for j in range(len(testcase[0])):
    if testcase[0][j] <= testcase[1][j]:
      d = (ord(testcase[1][j])-64) - (ord(testcase[0][j])-64)
    else:
      d= (ord(testcase[1][j])-64+26) - (ord(testcase[0][j])-64)

    d_list.append(d)

  print("Distances:", end=" ")
  for j in range(len(d_list)):
    print(d_list[j], end=" ")
  print()