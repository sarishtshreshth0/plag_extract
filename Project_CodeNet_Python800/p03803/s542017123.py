x = list(map(int, input().split()))
if x[0]==1:
    x[0]=14
if x[1]==1:
    x[1]=14
print("Alice" if x[0]>x[1] else "Bob" if x[0]<x[1] else "Draw")