n=int(input())
li = ["357","375","537","573","753","735"]
if n<1000:
  li=[s for s in li if int(s)<=n]
  print(len(li))
  exit()
t=["7","5","3"]
ans = 6
for i in range(4,10):
  li_new = []
  for s in li:
    for j in range(i):
      for k in t:
        u=int(s[:j]+k+s[j:])
        if u<=n:
          li_new.append(str(u))
  li=list(set(li_new))
  ans += len(li)
print(ans)