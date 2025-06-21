a, b, c, d = (int(i) for i in input().split())
l = [0] * 101

for i in range(a, b+1):
    l[i] += 1
    
for i in range(c, d+1):
    l[i] += 1
ans = 0
for i in l:
    if i == 2: ans += 1
print(max(ans-1, 0))
