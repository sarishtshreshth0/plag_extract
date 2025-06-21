import sys
A,B = map(int,input().split())
if A < 0 or A > 13 or B < 0 or B > 13:
    sys.exit()

if A == 1 or B == 1:
    if A == B:
        print("Draw")
    elif A == 1:
        print("Alice")
    elif B == 1:
        print("Bob")
    sys.exit()

if A > B:
    print("Alice")
elif B > A:
    print("Bob")
else:
    print("Draw")