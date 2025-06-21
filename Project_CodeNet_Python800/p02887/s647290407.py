N = int(input())
S = input()
S = S + "-"
ans = 0
for i in range(N):
    if S[i] != S[i + 1]:
        ans += 1
print(ans)
