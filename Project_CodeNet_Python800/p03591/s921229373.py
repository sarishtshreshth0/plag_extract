s = input()
if len(s) >= 4:
    print("Yes" if s == "YAKI" or s[:4] == "YAKI" else "No")
else:
    print("No")