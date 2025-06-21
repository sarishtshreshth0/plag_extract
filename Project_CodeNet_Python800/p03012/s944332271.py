n = int(input())
l = list(map(int, input().split()))

res = float('inf')
total = sum(l)
w = 0
for i in range(n):
    w += l[i]
    res = min(abs(w - (total - w)), res)
print(res)