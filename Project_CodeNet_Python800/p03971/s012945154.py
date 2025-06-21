import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))

n, a, b = MI()
s = input()
ok = 0
rank = 0
for si in s:
    if si == 'a':
        if ok < a+b:
            print("Yes")
            ok += 1
        else:
            print("No")
    elif si == 'b':
        rank += 1
        if ok < a+b and rank <= b:
            print("Yes")
            ok += 1
        else:
            print("No")
    else:
        print("No")