maxa=0
N=int(input())
L=list(map(int,input().split()))
c=[0]*100000
for i in L:
  c[i]+=1
for i in range(1,99999):
  s=c[i]+c[i-1]+c[i+1]
  maxa=max(maxa,s)
print(maxa)