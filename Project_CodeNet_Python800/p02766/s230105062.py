N,K =map(int,input().split())

count=0
while 1:
    if N//(K**count)==0:
        break
    count +=1
print(count)    
