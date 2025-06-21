a = list(map(int, input().split()))
n = int(input())
if n >= 2:
    if n % 2 == 0:
        print(int((n//2)*min(a[0]*8, a[1]*4, a[2]*2, a[3])))
    else:
        print(int((n//2)*min(a[0]*8, a[1]*4, a[2]*2, a[3])+min(a[0]*4, a[1]*2, a[2])))
else:
    print(min(a[0]*4, a[1]*2, a[2]))
