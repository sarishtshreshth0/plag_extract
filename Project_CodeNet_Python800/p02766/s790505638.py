N, K = map(int, input().split())

for n in range(10**10):
    if N < K**n:
        print(n)
        exit()