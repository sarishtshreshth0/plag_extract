A,B,C,D=map(int,input().split())
if C<=A and A<=D and D<=B:
    print(D-A)
elif C<=A and B<=D:
    print(B-A)
elif A<=C and C<=B and B<=D:
    print(B-C)
elif A<=C and D<=B:
    print(D-C)
else:
    print(0)