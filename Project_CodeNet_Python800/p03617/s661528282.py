Q, H, S, D = map(int, input().split())
N = int(input())

l = min(Q*4, H*2, S)
ll = min(l*2, D)
res = N//2*ll
if N % 2 == 1:
    res += l

print(res)