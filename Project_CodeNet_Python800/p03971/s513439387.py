n, a, b = map(int, input().split())
st = input()
c = a + b
for s in st:
    if s == "a":
        if c >= 1:
            c -= 1
            print("Yes")
        else:
            print("No")
    elif s == "b":
        if c >= 1 and b >= 1:
            c -= 1
            b -= 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")