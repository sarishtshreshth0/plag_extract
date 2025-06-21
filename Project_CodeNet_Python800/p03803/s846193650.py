A, B = map(int, input().split())

if (A == 1) and (B != 1):
    print("Alice")

elif (A != 1) and (B != 1) and (A > B):
    print("Alice")

elif (B == 1) and (A != 1):
    print("Bob")

elif (B != 1) and (A != 1) and (A < B):
    print("Bob")

elif (A == B):
    print("Draw")
