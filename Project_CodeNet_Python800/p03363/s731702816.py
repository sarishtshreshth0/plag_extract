from collections import Counter
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    cum = [0]*(N+1)
    for i in range(1,N+1):
        cum[i] = cum[i-1]+A[i-1]
    c = Counter(cum)
    ans = 0
    for v in c.values():
        ans += v*(v-1)//2
    return ans
print(solve())