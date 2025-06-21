import sys

N, M = map(int, input().split())
x = sorted(map(int, input().split()))

if N >= M:
    print(0)
    sys.exit()
diff = [0]*(M-1)
for i in range(M-1):
    diff[i] = x[i+1] - x[i]
diff.sort()
ans = sum(diff[:M-N])
print(ans)
