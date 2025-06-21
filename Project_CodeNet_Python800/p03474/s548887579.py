import os
import sys
import math
if os.environ.get("DEBUG") is not None:
    sys.stdin = open("in.txt", "r")
rl = sys.stdin.readline

a, b = map(int, rl().split())
s = rl().rstrip("\n")

failed = False
for i in range(0, a):
    if not 48 <= ord(s[i]) <= 57:
        failed = True
        break
if s[a] != "-":
    failed = True
for i in range(a + 1, len(s)):
    if not 48 <= ord(s[i]) <= 57:
        failed = True
        break
print("No" if failed else "Yes")