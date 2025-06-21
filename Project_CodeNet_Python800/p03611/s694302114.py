import collections

N = int(input())
a = [int(i) for i in input().split()]
g = a[:]
for i in g:
    a.append(i-1)
    a.append(i+1)



dict = collections.Counter(a)

for a, b in dict.most_common():
    print(b)
    break
