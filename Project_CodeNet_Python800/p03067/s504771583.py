A,B,C = map(int, open(0).read().split())
if A <= C <= B:
    print("Yes")
elif A >= C >= B:
    print("Yes")
else:
    print("No")