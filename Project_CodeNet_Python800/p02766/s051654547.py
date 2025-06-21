# B - Digits
N,K = map(int,input().split())
i = 1
while K**i-1<N:
    i += 1
print(i)