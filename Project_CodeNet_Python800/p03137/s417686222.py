n, m = map(int, input().split())
x = list(map(int, input().split()))

if n >= m:
    print(0)
    exit()

x.sort()

d = [x[i+1] - x[i] for i in range(m-1)]

d.sort()

print(sum(d[:m-n]))