n, r = map(int,input().split())

i=1
rr=r
while rr <= n:
    i+=1
    rr=rr*r
print(i)
