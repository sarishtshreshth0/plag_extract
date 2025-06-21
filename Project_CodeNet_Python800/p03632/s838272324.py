a, b, c, d = map(int, input().split())
aa = [0 for i in range(101)]
bb = [0 for i in range(101)]
ans = 0
for i in range(a, b):
    aa[i] = 1
for i in range(c, d):
    bb[i] = 1
for i in range(101):
    if aa[i] == 1 and bb[i] == 1:
        ans += 1
print(ans)