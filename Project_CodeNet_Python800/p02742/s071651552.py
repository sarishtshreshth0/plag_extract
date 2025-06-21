a = [int(c) for c in input().split()]
r = a[0]*a[1]
if a[0] == 1 or a[1] == 1:
    print(1)
elif r % 2 == 0:
    print(int(r/2))
else:
    print(int(r/2+1))
