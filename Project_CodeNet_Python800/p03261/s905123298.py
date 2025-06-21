n = int(input())

s = []
for _ in range(n):
    s.append(input())

it = iter(s)
for p, ne in zip(it, it):
    if p[-1] != ne[0]:
        print("No")
        exit()

if s[-2][-1] != s[-1][0]:
    print("No")
    exit()

if len(set(s)) == n:
    print("Yes")
else:
    print("No")
