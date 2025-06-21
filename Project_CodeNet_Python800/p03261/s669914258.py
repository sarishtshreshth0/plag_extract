N = int(input())
W = [input() for _ in range(N)]
ans = "Yes"

for i in range(N-1):
    if W[i][-1] != W[i+1][0] or W.count(W[i]) != 1:
        ans = "No"

print(ans)

