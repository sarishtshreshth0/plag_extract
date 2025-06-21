from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = []
for i in a:
    c.append(i)
    c.append(i-1)
    c.append(i+1)
c = Counter(c)

print(max(c.values()))
