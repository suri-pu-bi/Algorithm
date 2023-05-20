# defaultdict(): 딕셔너리를 만드는 dict클래스의 서브클래스
# 인자로 주어진 객체의 기본값을 딕셔너리값의 초깃값으로 지정할 수 있다.
# 처음 키를 지정할 때 값을 주지않으면 해당 키에 대한 값을 디폴트 값으로 지정하겠다.
from collections import defaultdict
from itertools import combinations


def solution(info, query):
    answer = []
    info_dict = defaultdict(list) # 값을 지정하지 않으면 빈 리스트로 초기화, 값을 지정하면 해당값으로 초기화

    # info를 가지고 dict 생성
    for i in info:
        row = i.split() # 공백기준 split
        info_keylist = row[:-1] # 나머지 값(언어, 직군, 경력, 소울푸드)을 key로
        info_value = int(row[-1]) # 점수값을 value로

        for i in range(5): # 언어, 직군, 경력, 소울푸드 4개 중
            for c in combinations(info_keylist,i):
                # 0개 선택, 1개 선택, 2개 선택, 3개 선택, 4개 선택
                info_key = "".join(c) #문자열로 바꿔서 key로 만들기
                # ex) javabackend, javabackendjunior
                info_dict[info_key].append(info_value)



    # 점수값들을 오름차순정렬 (이후 이분탐색을 위해)
    for key in info_dict.keys():
        info_dict[key].sort()


    # query 정리
    for q in query:
        qrow = q.split(' ') # query도 똑같이
        query_score = int(qrow[-1])
        query = qrow[:-1]

        for _ in range(3): # and는 공통적으로 3개가 있으므로
            query.remove('and') # remove: 맨 처음으로 만나는 단어만 삭제
        while '-' in query: # -가 있으면 -제거 -> 반복
            query.remove('-')
        query_key = ''.join(query) # 동일하게 key값을 문자열로 바꾸기

        # query_key가 info_dict 키에 있다면
        if query_key in info_dict:
            scoreList = info_dict[query_key] # 키에 맞는 점수들 뽑기

            # 이분탐색
            if len(scoreList)>0: # 점수가
                start=0
                end=len(scoreList)
                while start<end:
                    mid=(start+end)//2
                    if scoreList[mid] >= query_score: # query_score 점수보다 이상이면
                        end = mid # end를 mid로
                    else: # query_score 점수보다 미만이면
                        start = mid+1 # start를 mid+1로

                answer.append(len(scoreList)-start)

        # 쿼리에 해당하는 score가 없을 때
        else:
            answer.append(0)
    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]
print(solution(info, query))
