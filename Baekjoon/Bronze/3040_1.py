# Bronze 2
# 백설공주와 일곱 난쟁이

# 파이썬 라이브러리 조합이용
from itertools import permutations

dwarfs_9 = []
for i in range(9):
  dwarf = int(input())
  dwarfs_9.append(dwarf)

dwarfs_7 = list(permutations(dwarfs_9,7))
for dwarfs in dwarfs_7:
  if sum(dwarfs) == 100:
    for i in dwarfs:
      print(i)
    break