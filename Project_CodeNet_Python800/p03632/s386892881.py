A, B, C, D = map(int, input().split())

if A<=C and D<=B: 
    print(D-C)
    exit()

if C<=A and B<=D: 
    print(B-A)
    exit()


if (A<=C and C<= B and B<=D): 
    print(B-C)
    exit()

if C<=A and A<=D and D<=B: 
    print(D-A)
    exit()

if B<=C or D<=A: 
    print(0)
    exit()