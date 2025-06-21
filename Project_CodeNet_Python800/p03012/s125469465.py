n = int(input())
w = [int(s) for s in input().split()]

acc = [sum(w[:x]) for x in range(1, n + 1)]
center = acc[n - 1] / 2
index = 0

for i in range(n):
    if acc[i] >= center:
        if abs(center - acc[i]) < abs(center - acc[i - 1]):
            index = i
        else:
            index = i - 1
        break
print(abs((acc[n - 1] - acc[index]) - acc[index]))