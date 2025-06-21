n=int(input())
myarr=list(map(int,input().split()))
 
val=1000
 
for i in range(1,n):
    temp=abs(sum(myarr[0:i])-sum(myarr[i:]))
    val=min(val,temp)
 
print(val)