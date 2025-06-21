x = list(map(int, input().split()))
if x[0]<x[2]<x[1]:
    print("Yes")
elif x[1]<x[2]<x[0]:
    print("Yes")
else:
    print("No")