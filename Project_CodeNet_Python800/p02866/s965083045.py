N = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
    exit()

far = 0

cnt = [0 for i in range(N)]

for i in range(1, N):
    if D[i] == 0:
        print(0)
        exit()

    cnt[D[i]] += 1
    far = max(D[i], far)

ans = 1

for i in range(1, far):
    ans *= cnt[i] ** cnt[i + 1]

print(ans % 998244353)
