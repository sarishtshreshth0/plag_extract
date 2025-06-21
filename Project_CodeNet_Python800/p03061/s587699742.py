n = int(input())
raw = list(map(int,input().split()))
nn = 1
scale = 1
while True:
  if n <= nn:
    raw += [0] * (nn-n)
    break
  else:
    nn *= 2
    scale += 1
#print(raw,scale)
n = len(raw)

def gcd(aa,bb):
  if aa == 0:
    return bb
  elif bb == 0:
    return aa
  else:
    big,sml = aa,bb
    while sml:
      big,sml = sml,big%sml
    return big
seg = [0] * n + raw
for i in range(1,n)[::-1]:
  seg[i] = gcd(seg[2*i],seg[2*i+1])
#print(seg)
db = [2**i for i in range(scale)]
rdb = list(reversed(db))
#print(db)
#print(rdb)
can = []
for j in range(n):
  now = [[0,j],[j+1,db[-1]]]
  #print(now)
  g = 0
  for i in range(scale):
    last = now
    now = []
    for lr in last:
      l,r = lr
      if l == r:
        continue
      L = (l-1) // rdb[i] + 1
      R =   r   // rdb[i]
      if L < R:
        for U in range(L,R):
          g = gcd(g,seg[db[i]+U])
        now.append([l,rdb[i]*L])
        now.append([rdb[i]*R,r])
      else:
        now.append(lr)
      #print(now)
  can.append(g)
print(max(can))
#print(seg)