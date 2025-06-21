import bisect

n = int(input())
D = list(map(int, input().split()))
if D[0] != 0:
  print(0)
else:
  c = 1
  temp = 1
  e = 1
  D.sort()
  m = D[-1]
  if n > 1 and D[1] == 0:
    print(0)
    exit()
  else:
    for i in range(1, m+1):
      a = bisect.bisect_right(D, i)
      d = a - temp
      temp = a
      if d == 0 and i>0:
        print(0)
        exit()
      else:
        c *= e**d
        c %= 998244353
        e = d
    print(c)