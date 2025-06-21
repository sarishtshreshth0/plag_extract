n = int(input())
s = [0]
l = []
while s:
    p = s.pop()
    if p > n:
        continue
    l.append(p)
    s.append(p * 10 + 3)
    s.append(p * 10 + 5)
    s.append(p * 10 + 7)
ans = 0
for x in l:
    p = str(x)
    if p.count('3') and p.count('5') and p.count('7'):
        ans += 1
print(ans)
