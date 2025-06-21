n,k=map(int,input().split())
count = 0
while n/k >0:
    n//=k
    count+=1
print(count)