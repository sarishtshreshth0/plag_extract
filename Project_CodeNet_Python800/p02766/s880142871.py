N, K = list(map(int, input().split()))

cnt = 1
power = K

while power <= N:
    power *= K
    cnt += 1

print(cnt)