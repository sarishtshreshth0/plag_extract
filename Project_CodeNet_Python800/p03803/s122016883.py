a, b = map(int, input().split())
if a == 1:
    if b != 1:
        print("Alice")
        exit()
    else:
        print("Draw")
        exit()
elif b == 1:
    if a != 1:
        print("Bob")
        exit()
    else:
        print("Draw")
        exit()
 
if  a < b:
    print("Bob")
elif a > b:
    print("Alice")
else:
    print("Draw")