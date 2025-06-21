N,K = map(int,input().split())
for i in range(10*10):
    num = N // (K**i)
    if num < 1:
        print(i)
        exit()