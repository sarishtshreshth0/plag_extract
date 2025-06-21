N, K = map(int,input().split())
cnt = 0
while K ** cnt <= N:
    cnt += 1
print(cnt)