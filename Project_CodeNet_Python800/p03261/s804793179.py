N = int(input())
W = [input()]
for i in range(1, N):
    w = input()
    if w not in W and w[0] == W[i-1][-1]:
        W.append(w)
    else:
        print('No')
        exit()
print('Yes')
