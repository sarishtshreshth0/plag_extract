N = int(input())
S = input()
anchor = ''
ans = 0

for i in range(N):
    if anchor != S[i]:
        anchor = S[i]
        ans += 1

print(ans)