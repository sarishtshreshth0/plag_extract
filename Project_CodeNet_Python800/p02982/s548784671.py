(n,d),*xx = [list(map(int, s.split())) for s in open(0)]

from itertools import combinations

ans = 0
for i, j in combinations(range(n),2):
    s = sum((a-b)**2 for a,b in zip(xx[i],xx[j]))
    if s == round(s**0.5)**2:
        ans += 1

print(ans)