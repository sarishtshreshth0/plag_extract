import sys
input = sys.stdin.readline

n=int(input())
w = list(map(int,input().split()))
ans = sum(w)
for i in range(n):
    ans = min(ans,abs(sum(w[:i])-sum(w[i:])))
print(ans)