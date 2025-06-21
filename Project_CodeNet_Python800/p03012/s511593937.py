n = int(input())
w = list(map(int, input().split()))
p = [0 for i in range(n)]
p[0] = w[0]
for i in range(1, n):
    p[i] = p[i-1] + w[i]
diff = float('inf')
for j in range(n):
    cd = abs(p[n-1] - (2*p[j]))
    diff = min(diff, cd)
print(diff)