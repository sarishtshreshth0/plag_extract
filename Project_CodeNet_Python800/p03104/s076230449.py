import sys
input=sys.stdin.readline
def F(N):

    if not N & 1:
        x = N >> 1
        return x & 1
    return (N - 1) ^ F(N - 1)
A, B = map(int, input().split())
answer = F(B + 1) ^ F(A)
print(answer)