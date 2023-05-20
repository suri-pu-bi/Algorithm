# Sliver 4
# 설탕 배달 풀이 1

n = int(input())

bag_list = [5, 3]
count = 0
flag = False

for bag in bag_list:
    count += n // bag
    a = n % bag

    if a % 3 == 0:
        n = a
        flag = True

    else:
        while (count != 0 and a % 3 != 0):
            count -= 1
            a = n - (bag * count)
        n = a

if flag == False:
    count = -1

print(count)