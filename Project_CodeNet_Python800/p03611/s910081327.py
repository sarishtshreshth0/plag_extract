n = int(input())
num = list(map(int,input().split()))
lis = [0]*(max(num)+4)
for i in num:
    if i == 0:
        lis[i] +=1
        lis[i+1] +=1
    else:
        lis[i-1] +=1
        lis[i] +=1
        lis[i+1] +=1
    
print(max(lis))
