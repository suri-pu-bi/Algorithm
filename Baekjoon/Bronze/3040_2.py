# Bronze 2
# 백설공주와 일곱 난쟁이


# 설계) 전체 9개의 합에서 7개의 합이 100이 되도록 두 개씩 9개의 합에서 빼기

dwarfs = []

for i in range(9):
  dwarf = int(input())
  dwarfs.append(dwarf)

SUM = sum(dwarfs) # 전체 9개의 합

for i in range(0,8):
  for j in range(i+1,9):
    dwarfs_7 = SUM - dwarfs[i] - dwarfs[j]
    if dwarfs_7 == 100:
      a = i
      b = j
      break
      # break 한번만 하면 for문 한개만 탈출되므로 여기서 del하면 index 오류

del dwarfs[b]
del dwarfs[a]

for dwarf in dwarfs:
  print(dwarf)