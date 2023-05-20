# Bronze 1
# 일곱 난쟁이


dwarf = []
for i in range(9):
    height = int(input())
    if height not in dwarf and 1 <= height <= 100:
        dwarf.append(height)

sum_9 = sum(dwarf)
sum_2 = sum_9 - 100

breaker = False
not_dwarf = []
for i in range(9):
    for j in range(1, 9):
        not_dwarf_sum = dwarf[i] + dwarf[j]
        if not_dwarf_sum == sum_2:
            not_dwarf.append(dwarf[i])
            not_dwarf.append(dwarf[j])
            breaker = True
            break
        # break는 하나의 for문만 탈출
    if breaker == True:
        break

dwarf.remove(not_dwarf[0])
dwarf.remove(not_dwarf[1])

dwarf.sort()

for i in range(len(dwarf)):
    print(dwarf[i])