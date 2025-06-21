n = int(input())
w = list(map(int, input().split()))
z = []
for i in range(n):
    x = sum(w[:i])
    y = sum(w[i:])
    z.append(abs(x-y))
print(min(z))
