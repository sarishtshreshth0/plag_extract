n,k=map(int,input().split())
i=1
while True:
    if n>=k**i:
        i+=1
    else:
        break
print(i)