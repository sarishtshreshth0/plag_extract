n = int(input())
w = list(map(int, input().split()))

s = sum(w[1:])
t = w[0]

m = 100000

for i in range(1, n):
    m = min(m, abs(s-t))
    s -= w[i]
    t += w[i]

print(m)
