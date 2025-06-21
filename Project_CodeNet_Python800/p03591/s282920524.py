s = input()
l = len(s)
if l <= 3:
    print("No")
else:
    if s[:4] == "YAKI":
        print("Yes")
    else:
        print("No")