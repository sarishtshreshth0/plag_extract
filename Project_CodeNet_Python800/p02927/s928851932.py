x=input().split()
count=0
m=int(x[0])
n=list(x[1])
if len(n)==1:
    count=0
else:
    for d in range(2):
        n[d]=int(n[d])
    for i in range(4,m+1):
        for j in range(2,n[0]+1):
                for k in range(2,10):
                    if i==j*k:
                        count+=1
                        if j==n[0] and k>n[1]:
                            count-=1
print(count)