def f(x,y):
    A=0
    for i in range(len(x)):
        A+=(x[i]-y[i])*(x[i]-y[i])
    return A

M=20
N,D=map(int,input().split())

X=[]
for _ in range(N):
    X.append(tuple(map(int,input().split())))

S=set()
k=0
L=4*M*M*D
while k*k<=L:
    S.add(k*k)
    k+=1
    
K=0
for i in range(N):
    for j in range(i+1,N):
        K+=(f(X[i],X[j]) in S)
print(K)
