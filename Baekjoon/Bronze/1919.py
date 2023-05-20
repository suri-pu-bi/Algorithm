# Bronze 2
# 1919


str1 = list(input())
str2 = list(input())

# list.remove() 는 리스트를 변환 시킨 후 아무것도 반환하지 않음
# 그래서 remove의 반환값을 사용하려고 하면 Nonetype error 발생
# Error Code : str1 = str1.remove(str1[i])

# 리스트에서 요소를 삭제할 때, 앞에서부터 돌리면 indexerror 발생
# 뒤에서부터 for문을 돌리자

same_num1 = []
same_num2 = []

cnt = 0
for i in range(len(str1)):
  for j in range(len(str2)):
    if str1[i] == str2[j]:
      if j not in same_num2:
        same_num1.append(i)
        same_num2.append(j)
        break


# print(same_num1)
# print(same_num2)

ani1 = len(str1) - len(same_num1)
ani2 = len(str2) - len(same_num2)

# print(str1)
# print(str2)

print(ani1+ani2)