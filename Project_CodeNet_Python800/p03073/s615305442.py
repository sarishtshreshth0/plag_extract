S=list(map(int,input()))

X=0

Z=0
for s in S:
    if s!=Z:
        X+=1
    Z^=1
    
Y=0

Z=1
for s in S:
    if s!=Z:
        Y+=1
    Z^=1

print(min(X,Y))
