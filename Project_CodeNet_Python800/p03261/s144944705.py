N = int(input())
W = [input() for _ in range(N)]

if len(set(W)) != N:
    print('No')
    exit()

for i in range(1, N):
    if W[i][0] != W[i-1][-1]:
        print('No')
        exit()
print('Yes')
