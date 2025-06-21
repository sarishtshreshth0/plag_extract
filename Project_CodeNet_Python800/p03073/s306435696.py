S = list(input())
p = S.copy()

cnt1 = 0
cnt2 = 0
for i in range(1,len(S)):
    if S[i] == S[i-1]:
        if S[i] == '1':
            S[i] = '0'
        else:
            S[i] = '1'
        cnt1 += 1

for j in range(len(p)-2,-1,-1):
    if p[j] == p[j+1]:
        if p[j] == '1':
            p[j] = '0'
        else:
            p[j] = '1'
        cnt2 += 1

print(min(cnt1,cnt2))