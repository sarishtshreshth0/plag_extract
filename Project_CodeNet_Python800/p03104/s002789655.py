a,b = map(int,input().split())
am = a%4
bm = b%4
ad = a//4
bd = b//4
ans = 0
if ad == bd:
    for i in range(a, b+1):
        ans ^= i
else:
    while am != 0:
        ans ^= a
        a += 1
        am += 1
        am %= 4
    while bm != 3:
        ans ^= b
        b -= 1
        bm -= 1
        bm %= 4
print(ans)

