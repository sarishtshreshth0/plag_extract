N = int(input())
S = [input() for i in range(N)]

ans = 'Yes'
if len(S) != len(set(S)):
    ans = 'No'
for i in range(N-1):
    if S[i][-1] != S[i+1][0]:
        ans = 'No'
        break

print(ans)