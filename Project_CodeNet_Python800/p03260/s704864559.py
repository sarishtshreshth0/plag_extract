a, b = map(int, input().split())

ok = False
for i in range(1, 4):
    if (a * b * i) % 2 == 1:
        ok = True

if ok:
    print('Yes')
else:
    print('No')