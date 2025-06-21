a, b = map(int, input().split())
s = input()

flag = 0


if s[a] == "-":
    if s[:a].isdecimal() and s[a+1:].isdecimal():
        flag = 1
    else:
        flag = 0


if flag:
    print("Yes")
else:
    print("No")