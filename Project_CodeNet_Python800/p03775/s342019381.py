n = int(input())

l = []
for i in range(1, int(n ** 0.5)+1):
    if n % i == 0:
        l.append([i, n//i])

res = float('inf')
for a, b in l:
    res = min(res, max(len(str(a)), len(str(b))))

print(res)