A, B = map(int, input().split())
if A == B:
    print("Draw")
elif A != 1 and B != 1:
    if A < B:
        print("Bob")
    else:
        print("Alice")
elif A == 1:
    print("Alice")
elif B == 1:
    print("Bob")
