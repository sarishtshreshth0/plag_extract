n = int(input())
w = list(map(int,input().split()))

m = abs(sum(w[:1])-sum(w[1:]))
for i in range(1,n):
    t = abs(sum(w[:i])-sum(w[i:]))
    if m > t:
        m = t
print(m)
