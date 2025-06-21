N = int(input())
n = str(N)
l = len(n)
f = 0

for a in range(l):
    f += int(n[a])

if N%f == 0:
    print('Yes')
else:
    print('No')