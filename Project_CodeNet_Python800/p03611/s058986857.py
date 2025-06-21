N = int(input())
a = list(map(int, input().split()))
x = [0] * (10 ** 5 + 2)
for i in range(N):
    x[a[i]-1] += 1
    x[a[i]] += 1
    x[a[i]+1] += 1
print(max(x))
