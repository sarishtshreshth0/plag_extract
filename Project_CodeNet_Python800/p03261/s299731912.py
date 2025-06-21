N = int(input())
W = [input() for i in range(N)]

for i in W:
    if W.count(i) > 1:
        print('No')
        exit()

for i in range(1, N):
    if W[i - 1][-1] != W[i][0]:
        print('No')
        exit()

print('Yes')