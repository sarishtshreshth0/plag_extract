input()
*A,=map(int,input().split())
D=[0]*(10**7)

for a in A:
    D[a-1]+=1
    D[a]+=1
    D[a+1]+=1
print(max(D)) 