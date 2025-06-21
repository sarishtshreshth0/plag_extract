N = int(input())
W = []
for _ in range(N):
    W.append(input())

if len(set(W)) != len(W):
    print("No")
    exit(0)

for i in range(N-1):
    if W[i][-1] != W[i+1][0]:
        print("No")
        exit(0)

print("Yes")