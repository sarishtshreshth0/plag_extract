import itertools
import collections
N = int(input())
A = list(map(int, input().split()))
acum = [0] + list(itertools.accumulate(A))
acount = collections.Counter(acum)
print(sum(n * (n-1) // 2 for n in acount.values()))