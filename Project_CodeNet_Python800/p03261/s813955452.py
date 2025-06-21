N = int(input())

w = input().strip()
d = set([w])
l = w[-1]
f = True
for _ in range(N-1):
    w = input().strip()
    if w.startswith(l) and not w in d:
        d.add(w)
        l = w[-1]
    else:
        f = False
print("Yes" if f else "No")
