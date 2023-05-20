# Bronze 3
# 나는 요리사다

score_list = []


for i in range(0,5):
    score = input().split()
    score = list(map(int,score))
    # score = map(int,score) <map object at 0x00000244B945FC10> iterator 자체 반환되므로 list () 씌워주기
    s_score = sum(score)
    score_list.append(s_score)


winnerscore = max(score_list)
# max() list 요소들 중 최댓값 구하기
winner = score_list.index(winnerscore)
print(winner+1, winnerscore)
