# coding: utf-8
# Your code here!
N = int(input())
W = list(map(int,input().split()))
S = sum(W)
ans = float('inf')
for i in range(N):
    l = sum(W[:i+1])
    r = S - l
    ans = min(ans, abs(l-r))

print(ans)