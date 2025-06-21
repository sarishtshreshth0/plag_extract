n, m = map(int, input().split())
if n >= m:
    print(0)
    exit()

lx = sorted(list(map(int, input().split())))

ld = sorted([lx[i+1]-lx[i] for i in range(m-1)])
if n == 1:
    print(sum(ld))
else:
    print(sum(ld[:-(n-1)]))