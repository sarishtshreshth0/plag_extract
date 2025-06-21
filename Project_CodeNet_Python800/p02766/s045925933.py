N,K=map(int,input().split())
p,c=1,1
while p<=N:
    p*=K
    c+=1
print(c-1)