A,B,C,D=map(int,input().split())
s=max(A,C)
f=min(B,D)
if f-s>=0:
    print(f-s)
else:
    print(0)