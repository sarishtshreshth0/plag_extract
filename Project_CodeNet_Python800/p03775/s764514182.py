x = int(input())
ans = 10000
k = 1
while (k * k <= x):
    if (x%k == 0):
        j = max(len(str(int(x/k))), len(str(k)))
        ans = min(j, ans)
    k += 1
print(ans)