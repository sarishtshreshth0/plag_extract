import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n, a, b = inintm()
s = input()

rank = 1
tuka = 0

for i in range(n):
    if s[i] == "a":
        if tuka < a+b:
            print("Yes")
            tuka += 1
            continue
    elif s[i] == "b":
        if tuka < a+b and rank <= b:
            print("Yes")
            tuka += 1
            rank += 1
            continue
    print("No")
