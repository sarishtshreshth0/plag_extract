n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
val = []
if n >= m:
    print(0)
    exit()

for i in range(m-1):
    p = x[i+1]-x[i]
    val.append(p)
val.sort()
print(sum(val[:m-n]))