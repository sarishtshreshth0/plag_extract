A,B,C,D=map(int,input().split())
start=max(A,C)
goal=min(B,D)
dt=goal-start
if dt<0:
    print(0)
else:
    print(dt)