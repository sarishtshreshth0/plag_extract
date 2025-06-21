N = int(input())
W = []
for _ in range(N):
    w = input()
    W.append(w)

unique = list(set(W))
if len(unique) != N:
    print("No")
    exit()

for i in range(1, N):
    if W[i - 1][-1] != W[i][0]:
        print("No")
        exit()

print("Yes")
