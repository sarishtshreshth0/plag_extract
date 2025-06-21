from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
S = [0]*(N+1)
dic = defaultdict(int)
dic[0] = 1
for i in range(1,N+1):
    S[i] = S[i-1] + A[i-1]
    dic[S[i]] += 1
ans = 0
for _,v in dic.items():
    if v > 0:
        ans += v*(v-1)//2
print(ans)
