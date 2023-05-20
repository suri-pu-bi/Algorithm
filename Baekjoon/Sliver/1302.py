# Sliver 4
# 베스트셀러

n = int(input())

book_list = []
max_cnt = 0

for i in range(n):
    name = input()
    book_list.append(name)

book_list.sort()
i = 0
while i < len(book_list):
    cnt = book_list.count(book_list[i])
    if max_cnt < cnt:
        max_cnt = cnt
        book = book_list[i]
    i += cnt
    # for문 i+=cnt 해도 index값 안바뀜 => while문으로 고쳐서 해줘야함 (파이썬 특징)

print(book)
