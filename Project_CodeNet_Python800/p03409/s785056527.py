n=int(input())
f=lambda x:sorted([tuple(map(int,input().split())) for _ in range(n)],key=lambda k:k[x])
qr,qb=f(1)[::-1],f(0)
a=0
for c,d in qb:
  for i in range(n-a):
    if c>qr[i][0] and d>qr[i][1]: qr.pop(i); a+=1; break
print(a)