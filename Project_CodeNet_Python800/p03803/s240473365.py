A, B = map(int, input().split())
if A == B:
    print("Draw")
elif A == 1:
    print("Alice")
elif B == 1:
    print("Bob")
else:
    if A > B:
        print("Alice")
    else:
        print("Bob")