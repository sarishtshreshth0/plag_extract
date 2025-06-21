# k = 1 - nまでの k の和
def sigma1(n):
    return n * (n + 1) // 2

n = int(input())
dat = list(map(int, input().split()))
buf = [0] * (n+1)
cur = 0
import collections
pos = collections.defaultdict(list)

for i in range(0, n):
    cur += dat[i]
    pos[cur].append(i)
    buf[i+1] = cur

buf.sort()
#print(buf)
import collections
res = 0
c = collections.Counter(buf)
for k in c.keys():
    cnt = c[k]
    if cnt < 2:
        pass
    else:
        res += sigma1(cnt - 1)
print(res)
