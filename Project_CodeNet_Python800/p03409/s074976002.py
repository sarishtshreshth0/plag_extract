n=int(input());f=lambda x:sorted([list(map(int,input().split()))for _ in range(n)],key=lambda k:k[x]);r=f(1)[::-1];b=f(0);a=0
for c,d in b:
  for l in r:
    if c>l[0] and d>l[1]:r.remove(l);a+=1;break
print(a)