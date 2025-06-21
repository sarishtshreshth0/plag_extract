a, b = map(int, input().split())
c, d = a, b
l = []
m = []
n = []
t = 0
while b > 0:
    l.append(b%2)
    b //= 2
k = len(l)
for i in range(k):
    m.append(a%2)
    a //= 2
if d%2 == 1:
    l = [0]*(k)
if c%2 == 0:
    m = [0]*(k)
for i in range(k):
    n.append((l[i]+m[i])%2)
c = (c+1)//2*2
d = (d+1)//2*2
if (d-c)%4 == 2 or (d-c)%4 == 3:
    n[0] = (n[0]+1)%2
for i in range(k):
    t += n[i]*(2**i)
print(t)