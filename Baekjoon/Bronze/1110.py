# Bronze 1
# 더하기 사이클


N = input()
if int(N) >= 10:
    first = N
else:
    first = "0" + N

# print(first)
cnt = 0

while True:
    if int(N) >= 10:
        new = int(N) // 10 + int(N) % 10
        if new // 10 >= 1:
            n_number = N[1] + str(new)[1]
        else:
            n_number = N[1] + str(new)
        N = n_number
        cnt += 1
        # print(n_number)
        # print(cnt)

    else:
        n_number = str(int(N)) + str(int(N))
        N = n_number
        cnt += 1
        # print(n_number)
        # print(cnt)

    if first == n_number:
        print(cnt)
        break
