N = int(input())
W = [input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            if W[i] == W[j]:
                print("No")
                exit()
for k in range(N-1):
    if W[k][-1] != W[k+1][0]:
        print("No")
        exit()
print("Yes")