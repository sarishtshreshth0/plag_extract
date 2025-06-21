n, a, b = map(int, input().split())
s = list(input())
x, y = 0, 0
for i in s:
    if i == "a":
        if x + y < a + b:
            x += 1
            print("Yes")
        else:
            print("No")
    elif i == "b":
        if x + y < a + b and y < b:
            y += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")