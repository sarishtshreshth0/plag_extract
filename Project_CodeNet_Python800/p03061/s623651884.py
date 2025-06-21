from math import gcd
N = int(input())
A = list(map(int,input().split()))

front = [0] * N
front[0] = A[0]
for i in range(1,N):
    front[i] = gcd(front[i-1],A[i])
back = [0] * N
back[-1] = A[-1]
for i in reversed(range(N-1)):
    back[i] = gcd(back[i+1],A[i])

ans = max(front[-2],back[1])
for i in range(N-2):
    ans = max(ans,gcd(front[i],back[i+2]))
print(ans) 
