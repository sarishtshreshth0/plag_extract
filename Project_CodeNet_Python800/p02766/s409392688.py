N,K = map(int, input().split())
z = 1
cnt = 0
while z <= N:
    z *= K
    cnt += 1
print(cnt)