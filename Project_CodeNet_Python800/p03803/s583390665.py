a, b = map(int, input().split())
a -= 2
b -= 2
if a % 14 > b % 14:
    print("Alice")
elif a % 14 < b % 14:
    print("Bob")
else:
    print("Draw")
