from collections import defaultdict
N = int(input())
A = map(int, input().split(' '))
A = list(A)
s = [0] * (N+1)

for i in range(len(A)):
    s[i+1] = s[i] + A[i]

h = defaultdict(int)
ans = 0
for i, n in enumerate(s):
    ans += h[s[i]]
    h[s[i]] += 1

print(ans)
