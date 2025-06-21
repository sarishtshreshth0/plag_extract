s = input()
if len(s) < 4:
    print("No")
else:
    print("Yes" if s[:4] == "YAKI" else "No")