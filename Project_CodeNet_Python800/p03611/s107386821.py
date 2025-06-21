n=int(input())
a=list(map(int,input().split()))
maxi=-1
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for i in range(max(a)+1):
    maxi=max(maxi,(dic[i-1] if i-1 in dic else 0)+(dic[i] if i in dic else 0)+(dic[i+1] if i+1 in dic else 0))
print(maxi)