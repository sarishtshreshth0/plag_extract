n, m = map(int, input().split())
xlst = list(map(int, input().split()))
xlst.sort()
dlst = []
for i in range(m - 1):
    dlst.append(xlst[i + 1] - xlst[i])
dlst.sort(reverse = True)
ans = sum(dlst) - sum(dlst[:n - 1])
print(ans)