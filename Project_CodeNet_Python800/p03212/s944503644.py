import bisect
n = int(input())
l = len(str(n))
ary = []
siti = ["3","5","7"]
def dfs (s,t):
  if len(s) == t:
    if s.count("3") > 0 and s.count("5") > 0 and s.count("7") > 0:
      ary.append(int(s))
    return
  for j in siti:
    dfs(s+j,t)
for i in range(3,l+1):
  dfs("",i)
print (bisect.bisect_right(ary,n))
