import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
word = []

for i in range(n):
    w = input()
    if w in word:
        print("No")
        exit()
    if i != 0:
        if w[0] != word[i-1][-1]:
            print("No")
            exit()
    word.append(w)

print("Yes")