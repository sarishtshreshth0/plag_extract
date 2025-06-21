a,b=map(int,input().split())
if a==1:
    if a==b:
        print("Draw")
    else:
        print("Alice")
elif b==1:
    if a==b:
        print("Draw")
    else:
        print("Bob")
else:
    if a<b:
        print("Bob")
    elif a>b:
        print("Alice")
    else:
        print("Draw")