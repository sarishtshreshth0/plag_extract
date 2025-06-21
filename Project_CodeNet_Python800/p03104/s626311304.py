A, B = map(int,input().split())

# K以下の排他的論理和(K < 0 では 0を返す)
def solve(K):
    if K <= 3:
        ans = 0
        for i in range(K+1):
            ans ^= i
        return ans
    ans = ((K+1) // 2) % 2
    if K % 2 == 0:
        ans ^= K
    return ans
print(solve(A-1) ^ solve(B))