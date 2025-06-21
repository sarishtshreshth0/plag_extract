n=int(input())
lst=sorted(map(int,input().split()))

count=[0]*100001
for i in lst:
    if i==0:
        count[1]+=1
    else:
        count[i-1]+=1
        count[i]+=1
        count[i+1]+=1
        
print(max(count))