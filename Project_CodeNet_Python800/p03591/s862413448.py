s = input()

ans = 0

if (len(s) >= 4):
    if (s[0:4] == "YAKI"):
        ans = 1

if (ans == 1):
    print("Yes")
else:
    print("No")