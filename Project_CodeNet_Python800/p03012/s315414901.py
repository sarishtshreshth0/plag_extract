n = int(input())
w = list(map(int, input().split()))
a = []
x = 0
for i in range(n):
    x += w[i]
    a.append(x)

b = []
for j in range(n):
    b.append(abs(2 * a[j] - a[n - 1]))
print(min(b))