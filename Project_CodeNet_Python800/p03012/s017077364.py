n = int(input())
w = list(map(int,input().split()))

ans = abs(sum(w))
s1 = 0
s2 = sum(w)
for i in range(n-1):
    s1 += w[i]
    s2 -= w[i]
    m = abs(s2-s1)
    if m <= ans :
        ans = m
print(ans)
