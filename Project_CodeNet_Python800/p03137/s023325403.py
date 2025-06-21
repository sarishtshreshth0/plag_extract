n, m = map(int, input().split())
if n>=m:
    print(0)
    exit()
x = sorted(map(int, input().split()))
l = sorted(j-i for i, j in zip(x, x[1:]))[::-1]
print(x[-1]-x[0]-sum(l[:n-1]))