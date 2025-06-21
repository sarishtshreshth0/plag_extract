n, k =map(int, input().split())


for i in range(100):
    if n//(k**i) == 0:
        if n%(k**i)>=1:
            print(i)
            break
        else:
            print(i-1)
            break
