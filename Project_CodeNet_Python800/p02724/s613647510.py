X=int(input())
k=0
l=0
while X>=500:
    X-=500
    k+=1
while X>=5:
    X-=5
    l+=1
print(1000*k+5*l)