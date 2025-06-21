S = list(map(int, input()))

ans = 0
for i in range(1, len(S)):
    if S[i-1] == S[i]:
        S[i] = (S[i]+1)%2
        ans += 1

print(ans)
