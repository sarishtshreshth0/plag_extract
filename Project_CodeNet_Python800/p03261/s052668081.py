n = int(input())
w = [input() for _ in range(n)]
words_hist = set([])

last_letter = w[0][0]
for word in w:
    if word in words_hist:
        print('No')
        exit()
    if not word.startswith(last_letter):
        print('No')
        exit()
    
    words_hist.add(word)
    last_letter = word[-1]

print('Yes')