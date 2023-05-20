# Bronze 1
# 2007년

Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

for i in range(x - 1):
    Day = Day + arrList[i]
Day = (Day + y) % 7

print(weekList[Day])

# calendar module 사용
# import calendar

# arrList = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
# x, y = map(int,input().split())

# Day = calendar.weekday(2007, x, y)
# print(arrList[Day])
# '
