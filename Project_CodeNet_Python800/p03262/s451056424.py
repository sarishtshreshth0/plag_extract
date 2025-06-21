n, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
def euclid(a,b):
    if a % b == 0:
        return b
    else:
        return euclid(b, a%b)

now = abs(x[0] -x[1])
for i in range(1, len(x)-2):
    r = euclid(now, abs(x[i] - x[i+1]))
    if r < now:
        now = r
r = euclid(now, abs(x[0] - x[-1]))
if r < now:
    now = r
print(now)