# Bronze 1
# 단어 공부

word = input()
word = word.upper()
words = {}
for i in word:
  if i not in words:
    cnt = word.count(i)
    words[i] = cnt

# print(words)

# max(words): words의 key값 중 최댓값 출력
# key = words.get: value의 최댓값을 기준으로 하여 words의 key를 출력
# 한줄 for문/if문 사용시 빈 리스트 만들어서 추가하는 작업 불필요

max_word = [k for k,v in words.items() if max(words.values()) == v]
if len(max_word) >= 2:
  print("?")
else :
  print(max_word[0])