import collections

n = int(input())
a = list(map(int,input().split()))

for i in range(n):
    a.append(a[i] + 1)
    a.append(a[i] - 1)

l = collections.Counter(a)
l = list(l.values())
print(max(l))