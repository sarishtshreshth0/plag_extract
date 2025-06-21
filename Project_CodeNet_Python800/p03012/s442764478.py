N = int(input())
*W, =map(int,input().split())

B=[]
for i in range(N):
    A = abs(sum(W[0:i]) - sum(W[i:N]))
    B.append(A)
B.sort()    
print(B[0])   