A,B,C,D = map(int,input().split())
lower = max(A,C)
upper = min(B,D)
print(max(upper-lower,0))