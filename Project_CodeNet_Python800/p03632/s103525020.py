A, B, C, D = map(int,input().split())
a = min(B,D)
b = max(A,C)
if a-b>0:
    print(a-b)
else:
    print(0)