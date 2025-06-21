N, K = map(int,input().split())
i = 0
while True:
    if N/(K**i)<K:
        break
    i += 1

print(i+1)
