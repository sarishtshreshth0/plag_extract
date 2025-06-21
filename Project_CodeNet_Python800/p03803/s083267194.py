a, b = map(int, input().split())

if a == 1 and b == 1:
    print("Draw")
    exit()
elif a == 1:
    print("Alice")
    exit()
elif b == 1:
    print("Bob")
    exit()

if a == b:
    print("Draw")
elif a > b:
    print("Alice")
else:
    print("Bob")