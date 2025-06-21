I = lambda: map(int, input().rstrip().split())
a, b = I()
if (a > b or a == 1) and b != 1:
    print("Alice")
elif a == b:
    print("Draw")
else:
    print("Bob")