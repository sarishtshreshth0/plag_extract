Alice, Bob = map(int, input().split())

if Alice < Bob:
    if Alice == 1:
        print("Alice")
    else:
        print("Bob")
elif Alice > Bob:
    if Bob == 1:
        print("Bob")
    else:
        print("Alice")
else:
    print("Draw")