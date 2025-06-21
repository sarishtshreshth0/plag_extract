n=int(input())
A=list(map(int,input().split()))
D=[0 for i in range(10**7)]
for a in A:
    D[a-1]+=1
    D[a]+=1
    D[a+1]+=1
print(max(D))