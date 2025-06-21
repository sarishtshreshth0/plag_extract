n = int(input())
A = list(map(int, input().split()))
c = [0]*100000
ans = 0
for a in A:
    c[a] += 1

for i in range(1, 99999):
    cnt = c[i-1] + c[i] +c[i+1]
    ans = max(ans, cnt)

print(ans)