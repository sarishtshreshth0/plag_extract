from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
dd=defaultdict(lambda:0)
mina,maxa=0,10**5
for aa in a:
  mina=min(mina,aa)
  maxa=max(maxa,aa)
  dd[aa]+=1
maxsum=0
for i in range(mina, maxa-1):
  maxsum=max(maxsum, dd[i]+dd[i+1]+dd[i+2])
print(maxsum)