N = int(input())
W = [input() for _ in range(N)]

is_ok = (len(set(W)) == N)
for i in range(1, N):
    if W[i - 1][-1] != W[i][0]:
        is_ok = False

print("Yes" if is_ok else "No")