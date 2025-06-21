ri = lambda S: [int(v) for v in S.split()]
def rii(): return ri(input())

N, K = rii()

count = 0
while N:
    N //= K
    count += 1

print(count)
