from collections import defaultdict
N = int(input())
A = [0]+list(map(int,input().split()))
for i in range(N):
    A[i+1] += A[i]
dic = defaultdict(int)
for i in range(N+1):
    dic[A[i]] += 1
ans = 0
for x in dic.values():
    ans += x*(x-1)//2
print(ans)