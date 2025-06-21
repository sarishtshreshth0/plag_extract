import sys
from collections import Counter
readline=sys.stdin.readline

n=int(readline().strip())
a=list(map(int,readline().split()))

ea=Counter(a+list(map(lambda x:x+1,a)) + list(map(lambda x:x-1,a)))
print(max(list(ea.values())))