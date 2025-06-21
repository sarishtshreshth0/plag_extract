S = input()
N = len(S)

cnt1 = 0
cnt2 = 0
for s in S[::2]:
    if s == '0':
        cnt1 += 1
    elif s == '1':
        cnt2 += 1
for s in S[1::2]:
    if s == '1':
        cnt1 += 1
    elif s == '0':
        cnt2 += 1

print(N-max(cnt1, cnt2))