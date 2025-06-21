import itertools
import collections


n = int(input())

a = list(map(int,input().split()))
acu = [0] + list(itertools.accumulate(a))
cnt = collections.Counter(acu)
val = cnt.values()

ans = 0
for i in val:
    ans += i*(i-1)//2

print(ans)