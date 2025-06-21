n = int(input())
mlist = list(map(int,input().split()))
nlist =[]
for i in range(n):
  nlist.append(abs(sum(mlist[:i])-sum(mlist[i:])))
print(min(nlist))