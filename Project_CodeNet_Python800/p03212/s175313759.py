n = int(input())
import itertools
res = []
A = ['', '3', '5', '7']
for p in itertools.product(A, repeat=10):
    p = list(p)
    p = ''.join(p)
    if p.count('3') == 0 or p.count('5') == 0 or p.count('7') == 0:
        continue
    p = int(p)
    res.append(p)
res = list(set(res))
#print(res[0:10])
cnt = 0
for i in res:
    if i <= n:
        cnt += 1
print(cnt)
