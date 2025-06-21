N = int(input())
A = list(map(int, input().split()))
B=[]
C=[]
for i in range(N):
    B.append(A[i]-1)
for i in range(N):
    C.append(A[i]+1)
D=[]
D=A+B+C
mx=0
E=[0]*10**6
for i in D:
    E[i]+=1
    
print(max(E))