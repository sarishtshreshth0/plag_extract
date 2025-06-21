from collections import Counter
n, *a = map(int, open(0).read().split())
l = Counter(a)
for ai in a:
    l[ai+1] += 1
    l[ai-1] += 1
print(l.most_common()[0][1])