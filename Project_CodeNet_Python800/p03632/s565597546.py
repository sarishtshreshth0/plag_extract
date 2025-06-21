A,B,C,D=map(int,input().split())
if A<=C<=B:
    print(min(B,D)-C)
elif C<=A<=D:
    print(min(B,D)-A)
else:
    print(0)