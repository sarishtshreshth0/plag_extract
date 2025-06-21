a, b = list(map(int, input().split()))
if a == b:
    print("Draw")
else:
    if a != 1 and b != 1:
        if a > b:
            print("Alice")
        else:
            print("Bob")
    else:
        if a == 1:
            print("Alice")
        else:
            print("Bob")