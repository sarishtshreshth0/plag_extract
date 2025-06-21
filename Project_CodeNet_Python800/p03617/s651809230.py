Q, H ,S, D = map(int, input().split())
N = int(input())

tmp = [Q*4, H*2, S]
m = min(tmp)

if N == 1:
    print(m)
else:
    print(min(m*2, D) * (N//2) + m*(N%2))