a,b,c,d = map(int,input().split())
ab = [i for i in range(a,b+1)]
cd = [i for i in range(c,d+1)]

inter = set(ab).intersection(set(cd))

if len(inter) != 0:
  print(len(inter) - 1)
else:
  print(0)