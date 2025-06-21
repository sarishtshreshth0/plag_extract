n = int(input())
w = [int(i) for i in input().split()]
d = sum(w)
for wi in w:
    if d - 2 * wi < 0:
        print(min(d, 2 * wi - d))
        break
    d -= 2 * wi
