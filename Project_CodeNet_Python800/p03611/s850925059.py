n,*a=map(int,open(0).read().split())
b=[q-1 for q in a]
c=[q+1 for q in a]
from collections import Counter
d=a+b+c
e=Counter(d)
print(e.most_common()[0][1])