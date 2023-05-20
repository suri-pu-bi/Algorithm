# Bronze 2
# 과제 안 내신 분 ..?

student_list = []
num_list = list(range(1, 31))

for i in range(28):
    n = int(input())
    student_list.append(n)

student_list.sort()

for i in range(28):
    if student_list[i] != num_list[i]:
        print(num_list[i])
        del num_list[i]
        if len(num_list) == 28:
            break

if 29 in num_list and len(num_list) == 29:
    print(30)

elif 30 in num_list and len(num_list) == 29:
    print(29)

elif len(num_list) == 30:
    print(29)
    print(30)

# 색다른 방법 접근
# data = [0] * 31

# for i in range(28) :
#   n = int(input())
#   data[n] = 1

# for i in range(1, 31) :
#   if data[i] == 0 :
#     print(i)