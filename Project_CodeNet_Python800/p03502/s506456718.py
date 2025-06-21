N = int(input())
ans = 0
t = N
while 1:
    ans += t % 10
    t = t // 10
    if t == 0:
        break
print("Yes" if N % ans == 0 else "No")
