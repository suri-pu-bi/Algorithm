# Bronze 1
# 슈퍼 마리오


mushroom_list = []
for i in range(10):
    mushroom = int(input())
    mushroom_list.append(mushroom)

# print(mushroom_list)

b_score = 0
for i in range(9):
    b_score = b_score + mushroom_list[i]
    a_score = b_score + mushroom_list[i + 1]
    # print(b_score, a_score)
    if a_score >= 100 and b_score <= 100 and 100 - b_score >= a_score - 100:
        print(a_score)
        break
    elif a_score >= 100 and b_score <= 100 and 100 - b_score < a_score - 100:
        print(b_score)
        break
    elif a_score < 100 and b_score < 100 and i == 8:
        print(a_score)
        break
