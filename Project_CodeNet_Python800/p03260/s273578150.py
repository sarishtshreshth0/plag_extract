a, b = map(int, input().split())
while True:
    if a*b*1 % 2 != 0:
        print("Yes")
        break

    elif a*b*2 % 2 != 0:
        print("Yes")
        break

    elif a*b*3 % 2 != 0:
        print("Yes")
        break

    else:
        print("No")
        break
