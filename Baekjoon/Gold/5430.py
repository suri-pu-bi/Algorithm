# Gold 5
# AC

# 함수 R: 배열에 있는 수의 순서를 뒤집는 함수
# 함수 D: 첫번째 수를 버리는 함수 , 배열 비어있을 때 D를 사용한 경우 에러 발생
# ex) RDD: 연속 수행 함수, 배열을 뒤집은 다음, 다음 처음 두수를 버리는 함수
# p,n이 매우 큼 -> 시간초과 우려
# DP인가? 투포인터? deque 이용 (굳이 반전하지 않아도 됨)


def ac(p, number_list):
    cnt = 0
    for i in range(len(p)):
        if p[i] == 'R':
            cnt += 1  # 배열의 뒤에서 원소를 빼야하므로 카운트 하나씩 증가

        else:
            if not number_list:
                return "error"
            else:
                if cnt % 2 == 0: # cnt가 짝수이면 원래 배열이므로
                    number_list.popleft() # 원래의 배열에서 앞에서 수를 빼기
                else: # cnt가 홀수이면 배열을 뒤집에서 앞에서 빼는 것이므로
                    number_list.pop() # 원래의 배열에서 뒤에서 수를 빼기


    if cnt % 2 != 0:
        number_list.reverse()

    return '[' + ','.join(number_list) + ']' # 출력초과 해결: 리스트를 문자열로 출력


from collections import deque

import sys
t = int(sys.stdin.readline())

for i in range(t):
    p = sys.stdin.readline().rstrip() # 오른쪽 공백 제거
    n = int(sys.stdin.readline())

    # 리스트 입력 처리가 관건!
    number_list = sys.stdin.readline().rstrip()[1:-1] # 끝에 '['랑 ']' 없애기

    if len(number_list) > 1: # ['']의 길이는 1 예외처리
        number_list = number_list.split(",")
    number_list = deque(number_list)

    print(ac(p,number_list))


