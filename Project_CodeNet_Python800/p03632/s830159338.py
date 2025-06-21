A,B,C,D=map(int,input().split())
L=max(A,C)
R=min(B,D)
print(max(0,R-L))