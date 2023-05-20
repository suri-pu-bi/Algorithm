# Bronze 2
# 블랙잭

import itertools
# 조합, 순열

N, M = map(int,input().split())
cards = list(map(int,input().split()))
cards3 = itertools.combinations(cards,3)

sum_ = []
for card in cards3:
  card = list(card)
  if sum(card)<= M :
    sum_.append(sum(card))

print(max(sum_))
