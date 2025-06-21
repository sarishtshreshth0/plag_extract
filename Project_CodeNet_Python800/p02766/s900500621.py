n,k=map(int, input().split())

count=1
quo=n//k

while quo>0:
    quo=quo//k
    count+=1

print(count)