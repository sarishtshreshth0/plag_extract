n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
if n >= m:
    print(0)
    exit()
l = [0 for _ in range(m-1)]
for i in range(m-1):
    l[i] = x[i+1] - x[i]
l.sort(reverse=True)
print(sum(l[n-1:]))