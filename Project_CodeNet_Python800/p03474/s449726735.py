import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a, b = inintm()
s = input()

x = 0
y = 0

try:
    x = int(s[:a])
    y = int(s[a+1:])
except:
    print("No")
    exit()

if s[a] == "-":
    print("Yes")
else:
    print("No")
