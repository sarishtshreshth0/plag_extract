A,B,C,D=input().split()
A=int(A)
B=int(B)
C=int(C)
D=int(D)

if min(B,D)-max(A,C)>0:
    ans=min(B,D)-max(A,C)
else:
    ans=0
print(ans)