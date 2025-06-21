# B - Shiritori
N = int(input())
W = [str(input()) for _ in range(N)]

ans = "Yes"
for i in range(N-1):
    if W.count(W[i]) > 1:
        ans = "No"
        break
    if W[i][-1] != W[i+1][0]:
        ans = "No"
        break

print(ans)
