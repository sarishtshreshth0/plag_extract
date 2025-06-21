i = [p+2 for p in range(12)]
i.append(1)
x, y = map(int, input().split())
if i.index(x) == i.index(y):
    print("Draw")
if i.index(x) > i.index(y):
    print("Alice")
if i.index(x) < i.index(y):
    print("Bob")
