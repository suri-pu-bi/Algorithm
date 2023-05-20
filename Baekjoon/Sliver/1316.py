# Sliver 5
# 그룹 단어 체커

def checker(word):
    flag = True
    cnt = 0

    if len(word) == 1:
        cnt = 1
    elif word.count(word[0]) == len(word):
        cnt = 1
    elif len(word) == len(set(word)):
        cnt = 1

    elif len(word) != len(set(word)) and word.count(word[0]) != len(word) and len(word) != 1:
        words = list(word)
        num = 0
        while num < len(words):
            count = words.count(words[num])
            # print("))",count)
            if count > 1:
                index_list = []
                index = num
                index_list.append(index)
                for j in range(1, count):
                    index = words.index(words[num], index + 1)
                    index_list.append(index)
                # print(index_list)
                for k in range(len(index_list) - 1):
                    if index_list[k] + 1 != index_list[k + 1]:
                        flag = False
                        break
                    else:
                        flag = True

                num = num + len(index_list)


            else:
                num += 1

            if flag == False:
                break

        if flag == True:
            cnt = 1

    return cnt


N = int(input())
cnt = 0
for i in range(N):
    word = input()
    cnt += checker(word)

print(cnt)
