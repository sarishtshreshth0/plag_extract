A,B = list(map(int,input().split()))
listA = list(range(2,14))
listA.append(1)
C = listA.index(A)
D = listA.index(B)
if C > D:
    print("Alice")
elif C == D:
    print("Draw")
else:
    print("Bob")