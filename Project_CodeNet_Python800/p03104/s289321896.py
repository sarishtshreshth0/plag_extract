a,b = map(int,input().split())
ans = 0
if b-a <= 4:
    for x in range(a, b+1):
        ans ^= x
else:
    s = a%4
    t = b%4
    if s == 0:
        s = 4
    for x in range(a, a+4-s):
        ans ^= x
    for x in range(b-t, b+1):
        ans ^= x
print(ans)