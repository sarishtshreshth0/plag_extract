n = int(input())
words = [input() for i in range(n)]
mae = ''
ans = 'Yes'

for i in range(n):
    if i == 0:
        word = words[0]
        leng = len(word)
        mae = word[leng-1]
    else:
        word = words[i]
        if mae != word[0:1] or words.count(word) >= 2:
            ans = 'No'
            break
        else:
            leng = len(word)
            mae = word[leng-1]

print(ans) 