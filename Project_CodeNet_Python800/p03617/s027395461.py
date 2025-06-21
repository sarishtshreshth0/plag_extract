Q, H, S, D = map(int, input().split())
N = int(input())*4
arr = [[Q, Q, 1], [H/2, H, 2], [S/4, S, 4], [D/8, D, 8]]
arr.sort()
ans = 0
for _, cost, size in arr:
    ans += (N//size)*cost
    N %= size
    if N == 0: break
print(ans)
