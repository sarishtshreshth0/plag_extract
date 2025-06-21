N = int(input())
S = input()

ans = 0
p = S[0]
for i in range(1, N):
    if S[i] == p:  continue
    else:
        ans += 1
        p = S[i]
print(ans + 1)