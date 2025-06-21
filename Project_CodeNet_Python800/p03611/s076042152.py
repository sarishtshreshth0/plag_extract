N = int(input())
A = list(map(int, input().split()))
C = [0]*(10**5)
for ai in A:
    C[ai] += 1

ans = 0
for i in range(10**5-2):
    ans = max(C[i] + C[i+1] + C[i+2], ans)
print(ans)