A,B,C,D=map(int,input().split())
d=min(B,D)-max(A,C)
print(d if d>=0 else 0)