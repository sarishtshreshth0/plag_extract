import sys
sys.setrecursionlimit(10**5) #再帰回数を増やさないとREになる

N, M, K = map(int, input().split())
friend = [[] for _ in range(N)]
block = [[] for _ in range(N)]
for _ in range(M):
  a, b = map(int, input().split())
  friend[a-1].append(b-1)
  friend[b-1].append(a-1)
for _ in range(K):
  c, d = map(int, input().split())
  block[c-1].append(d-1)
  block[d-1].append(c-1)

sgn = [0 for _ in range(N)]
groupnum = 0

def makenetwork(n, groupnum):
  for item in friend[n]:
    if sgn[item] == 0:
      sgn[item] = groupnum
      makenetwork(item, groupnum)

for k in range(N):
  if sgn[k] == 0:
    groupnum += 1
    sgn[k] = groupnum
    makenetwork(k, groupnum)

count = [0 for _ in range(groupnum)]
for k in range(N):
  count[sgn[k]-1] += 1

ans = ''
for k in range(N):
  num = count[sgn[k]-1] -1  - len(friend[k])
  for item in block[k]:
    if sgn[item] == sgn[k]:
      num -= 1
  ans += str(num) + ' '

ans.rstrip()
print(ans)