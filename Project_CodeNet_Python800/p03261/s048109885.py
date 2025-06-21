n = int(input())
wordlist = []
for i in range(n):
    word = str(input())
    if word in wordlist:
        print('No')
        exit()
    if wordlist and wordlist[-1][-1] != word[0]:
        print('No')
        exit()
    wordlist.append(word)
print('Yes')