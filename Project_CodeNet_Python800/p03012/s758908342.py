n = int(input())
w = list(map(int,input().split()))
s0 = float('inf')
for i in range(1,n):
    s0 = min(s0,abs(sum(w[:i])-sum(w[i:])))
print(s0)