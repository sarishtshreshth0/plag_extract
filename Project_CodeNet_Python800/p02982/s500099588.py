import math

N,D=map(int,input().split())

arr=[list(map(int,input().split())) for i in range(N)]
count=0

def dis(x,y):
    a=0
    for i in range(len(x)):
        a+=(x[i]-y[i])*(x[i]-y[i])
    return math.sqrt(a)
    
for i in range(N-1):
    for j in range(i+1,N):
        if dis(arr[i],arr[j])%1==0:
            count+=1

print(count)
