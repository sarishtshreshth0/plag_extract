from itertools import *
from collections import *
input()
A=list(accumulate(map(int,input().split())))
print(sum(n*(n-1)//2 for n in Counter(A+[0]).values()))