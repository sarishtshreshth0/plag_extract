n = int(input())
w = list(map(int, input().split()))

s = sum(w)
t = 0
res = 10**18
for ww in w:
    t += ww
    res = min(abs(s-t-t), res)
print(res)
