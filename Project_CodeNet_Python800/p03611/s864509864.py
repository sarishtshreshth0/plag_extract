from collections import Counter
N = int(input())
A = list(map(int, input().split()))
A.sort()
C = Counter(A)
ma = max(2, A[-1])
L = [0]*(ma+1)
for i in range(ma+1):
    l = C.get(i)
    if l == None:
        l = 0
    L[i] = l
# print(L)
ans = [0]*(ma-1)
ans[0] = L[0]+L[1]+L[2]
for i in range(1, ma-1):
    ans[i] = ans[i-1]-L[i-1]+L[i+2]
# print(ans)
print(max(ans))
