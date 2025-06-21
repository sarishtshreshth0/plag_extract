n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())), reverse=True)
l = sorted([a[i-1] - a[i] for i in range(1, m)], reverse=True)
print(sum(l[n-1:]))
