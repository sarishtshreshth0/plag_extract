import collections
n=input()
a=list(map(int, input().split()))

b=map(lambda x: x+1, a)
c=map(lambda x: x-1, a)
b=list(b)
c=list(c)

for num in range(len(a)):
    a.append(b[num])
    a.append(c[num])

d=collections.Counter(a)
values,counts=zip(*d.most_common())
print(counts[0])