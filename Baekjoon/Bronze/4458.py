# Bronze 3
# 첫 글자를 대문자로

N = int(input())

sen_ = []
for i in range(N):
    sen = input()
    # if sen[0].islower() :
    # str이 소문자인지 아닌지 검사
    sen = sen[0].upper() + sen[1:]
    # sen.upper()만 한다고 해서 sen이 바뀌는 것이 아님
    # 반환값이 있으므로 변수에 저장해야해서 출력해야함
    # python 문자열은 변경할 수 없음 sen[0] = sen[0].upper()로 바꿀 수 없음
    # -> 그러고 싶으면 list로 고쳐야함
    # elif sen[0].isupper() :
    # pass

    sen_.append(sen)

for i in range(N):
    print(sen_[i])