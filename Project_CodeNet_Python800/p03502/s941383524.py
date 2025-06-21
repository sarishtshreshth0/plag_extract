N=input()
S=list(map(int,N))
X=sum(S)
f=int(N)%X
print('Yes' if int(N)%X==0 else 'No')
