import sys

n = int(input())
s = list(input())

if n == 1:
    print(1)
    sys.exit()

a = []

for i in range(n-1):
    if s[i] != s[i+1]:
        a.append(s[i])

if len(a) == 0:
    print(1)
else:
    if a[-1] != s[-1]:
        a.append(s[-1])

    print(len(a))
