a = True
n = int(input())
p = input()
s = {p}
for i in range(n-1):
    c = input()
    if p[-1] != c[0] or c in s:
        a = False
    else:
        p = c
        s.add(p)
if a:
    print('Yes')
else:
    print('No')