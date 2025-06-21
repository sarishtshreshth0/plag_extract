Q,H,S,D = map(int, input().split())
N = int(input())
Q *= 4
H *= 2
min_cost = min(Q,H,S)
res = 0
if N%2:
    N -= 1
    res += min_cost
if N != 0:
    res += N//2*min(2*min_cost,D)
print(res)