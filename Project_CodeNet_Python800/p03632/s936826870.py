A,B,C,D = map(int,input().split())
if max(A,C) <= min(B,D):
    print(abs(max(A,C)-min(B,D)))
else:
    print(0)
