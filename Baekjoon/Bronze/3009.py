# Bronze 3
# 네번쨰 점

x_ = []
y_ = []

for i in range(3):
  x, y = map(int,input().split())
  x_.append(x)
  y_.append(y)


for i in range(3):
  cntx = x_.count(x_[i])
  if cntx == 1:
    x = x_[i]
  cnty = y_.count(y_[i])
  if cnty == 1:
    y = y_[i]

print(x,y)