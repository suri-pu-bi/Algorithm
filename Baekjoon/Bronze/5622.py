# Bronze 2
# 다이얼

a = 65
alphabet = []
words = input()
for i in range(8):
    if a == 80 or a == 87:
        alphabet.append(list(map(chr, range(a, a + 4))))
        a = a + 4
        # print(a, alphabet)
    else:
        alphabet.append(list(map(chr, range(a, a + 3))))
        a = a + 3
        # print(a, alphabet)

# print(alphabet)
# print(alphabet[0])
## dial = ['ABC','DEF', 'GHI', 'JKL', 'MNO','PQRS', 'TUV','WXYZ'] -> code easy

time = 0
for i in range(len(words)):
    for j in range(8):
        if words[i] in alphabet[j]:
            time = time + 3 + j

print(time)
