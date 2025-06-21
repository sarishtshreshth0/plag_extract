A, B = map(int,input().split())

# K以下の排他的論理和
def solve(K):
    ans = ((K+1) // 2) % 2
    if K % 2 == 0:
        ans ^= K
    return ans

print(solve(A-1) ^ solve(B))