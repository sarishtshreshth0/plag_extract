n, a, b = map(int, input().split())
s = input()
A = 0
B = 0
for i in range(len(s)):
    if s[i] == "a":
        if A + B < a + b:
            print("Yes")
            A += 1
        else:
            print("No")
    elif s[i] == "b":
        if A + B < a + b and B < b:
            print("Yes")
            B += 1
        else:
            print("No")
    else:
        print("No")