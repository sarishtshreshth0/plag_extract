from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
S = [0]*(N+1)
for i in range(1,N+1):
    S[i] = S[i-1] + A[i-1]
ans = 0
dic = defaultdict(int)
for i in range(N+1):
    ans += dic[S[i]]
    dic[S[i]] += 1
print(ans)
