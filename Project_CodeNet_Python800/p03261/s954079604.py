n = int(input())
w = [input() for i in range(n)]
x = w[0][0]
s = set()
flag = True
for wi in w:
    if wi[0] != x or wi in s:
        flag  = False
        break
    else:
        x = wi[-1]
        s.add(wi)
print("Yes" if flag else "No")