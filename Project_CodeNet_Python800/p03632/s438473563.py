x=list(map(int,input().split()))
if x[1]<x[3]:
    x=x
elif x[1]>x[3]:
    x=[x[2],x[3],x[0],x[1]]
else:
    x=[min(x[0],x[2]),x[1],max(x[0],x[2]),x[3]]
a,b,c,d=x

print(max(0,b-c) if a<c else b-a)