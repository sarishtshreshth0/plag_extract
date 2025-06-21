S = input().rstrip()
L = len(S)
cnt = 0
for i in range(L):
    if int(S[i]) != i%2:
        cnt += 1
print(min(cnt, L-cnt))