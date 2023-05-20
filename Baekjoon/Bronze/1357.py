# Bronze 1
# 뒤집힌 덧셈

# 파이썬에서는 문자열 수정 불가

def Rev(x):
    for i in range(len(x) // 2):
        temp = x[i]
        x[i] = x[len(x) - 1 - i]
        x[len(x) - 1 - i] = temp

    x = int("".join(x))
    return x


x, y = input().split()
x = Rev(list(x))
y = Rev(list(y))
# map 함수의 반환 값은 map객체 이기 때문에 해당 자료형을 list 혹은 tuple로 형 변환시켜야함
# map(function,순회가능한 객체)
z = list(map(str, str(x + y)))
print(Rev(z))