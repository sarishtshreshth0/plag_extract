def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

n, x = map(int,input().split())
arr = list(map(int,input().split()))
diff = []
arr.sort()
g = abs(arr[0] - x)
for i in range(1,n):
    g = gcd(g, abs(arr[i] - x))
print(g)