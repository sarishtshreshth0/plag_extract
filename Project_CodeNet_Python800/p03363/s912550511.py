N = int(input())
A = [int(i) for i in input().split()]

S = [0] * (N + 1)
for i in range(1, N+1):
    S[i] = S[i-1] + A[i-1]

dict = {}
for i in range(N+1):
    s = S[i]
    if s not in dict:
        dict[s] = 1
    else:
        dict[s] += 1

ans = 0
for s in dict.values():
    ans += s * (s - 1) // 2

print(ans)