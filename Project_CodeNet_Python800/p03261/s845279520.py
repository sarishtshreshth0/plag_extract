N = int(input())
W = [input() for _ in range(N)]
words = [''] * N
for i in range(N):
    if i == 0:
        words[i] = W[i]
        continue
    if (W[i] in words) or (W[i - 1][-1] != W[i][0]):
        print('No')
        break
    words[i] = W[i]
else:
    print('Yes')
