# Bronze 2
# 도비의 영어 공부

cnt_list = []
while True:
    sen = input()
    sen_ = sen.split()  # 문자열을 공백을 구분자로 나누어 리스트 생성 ('a'/a를 구분자로 나누어 리스트 생성)
    if sen_[0] == "#":
        break
    cnt_list.append(sen_[0])
    sen__ = (' ').join(sen_[1:])
    # print(sen__)
    sen__ = sen__.lower()
    # print(sen__)
    cnt = sen__.count(sen_[0])
    cnt_list.append(cnt)
for i in range(0, len(cnt_list), 2):
    print(cnt_list[i], cnt_list[i + 1])
