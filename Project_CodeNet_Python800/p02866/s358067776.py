n=int(input())
d=list(map(int,input().split()))
if d[0]!=0:
    print(0)
    exit()
del d[0]
for i in range(n-1):
    if d[i]==0:
        print(0)
        exit()
dcnt=[0]*(n)
for i in range(n-1):
    dcnt[d[i]]+=1
for j in range(n-1,-1,-1):
    if dcnt[j]==0:
        del dcnt[j]
    else:
        break
if len(dcnt)==0:
    print(0)
    exit()
dcnt[0]=1
sum=1
for i in range(1,len(dcnt)):
    sum*=pow(dcnt[i-1],dcnt[i])
    sum%=998244353
print(sum)
