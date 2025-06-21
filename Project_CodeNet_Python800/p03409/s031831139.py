n = int(input())

AB = [list(map(int, input().split())) for _ in range(n)]
CD = [list(map(int, input().split())) for _ in range(n)]

Red = sorted(AB, key=lambda x: x[1], reverse = True)
Blue = sorted(CD, key= lambda x: x[0])

ans = 0
for b in Blue:
    for r in Red:
        if r[0] < b[0] and r[1] < b[1]:
            ans += 1
            Red.remove(r)
            break

print(ans) 