n, m = list(map(int, input().split()))
x = list(map(int, input().split()))

x = sorted(x)
dist = [x[i+1] - x[i] for i in range(len(x) - 1)]

dist = sorted(dist)

if n == 1:
    print(sum(dist))
else:
    print(sum(dist[:-(n-1)]))