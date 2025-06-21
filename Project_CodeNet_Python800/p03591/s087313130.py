from sys import stdin
s = stdin.readline().rstrip()

if s[:4] == "YAKI":
    print("Yes")
else:
    print("No")