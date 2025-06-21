import math
from bisect import bisect_right
from copy import copy
n = int(input())
li = set([357,375,537,573,735,753])
li2 = set()
for i in li:
    li2.add(str(i))
li4 = copy(li2)
for k in range(6):
    li3 = set()
    for i in li4:
        for j in range(len(i)):
            i1 = i[:j]+'3' +i[j:]
            i2 = i[:j]+'5' +i[j:]
            i3 = i[:j]+'7' +i[j:]
            li3.add(i1)
            li3.add(i2)
            li3.add(i3)
    li4 = copy(li3)
    for j in li4:
        li2.add(j)
li5 = []
for i in li2:
    li5.append(int(i))
li5.sort()
k = bisect_right(li5, n)
print(k)