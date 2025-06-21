N, K = [int(x) for x in input().split()]

l = []

while N > 0:
    l.insert(0, N % K)
    N = N // K

print(len(l))
