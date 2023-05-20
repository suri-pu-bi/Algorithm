# Bronze 1
# 펠린드롬수

while(True):
  num = input()
  if int(num) == 0:
    break
  else:
    for i in range(len(num)):
      j = len(num)-1-i
      if num[i] != num[j]:
        print("no")
        break
      else:
        if j==len(num)//2: # 두번 반복 없애기
          print("yes")
          break
