n = int(input())
w = list(map(int,input().split()))
sumw = sum(w)
s1 = 0
sa = abs(sumw - s1)
for i in range(n):
    s1 += w[i]
    sumw -= w[i]
    if sa >= abs(sumw-s1):
        sa = abs(sumw-s1)
print(sa)