n = int(input())
w = list(map(int, input().split()))

Wl = [0]
for i in range(n):
    Wl.append(Wl[i]+w[i])

a = 100000

for i in range(n+1):
    a = min(abs(-Wl[i] - Wl[i] + Wl[n]), a)

print(a)

