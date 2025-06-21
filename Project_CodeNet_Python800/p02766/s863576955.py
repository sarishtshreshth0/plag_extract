n,k = list(map(int, input("").split()))
out=1
while n/k**out>=1:
    out+=1
print(out)