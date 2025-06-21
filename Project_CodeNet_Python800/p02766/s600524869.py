N,K = map(int,input().split())

D = 1
while True:
    if N//K >0:
        D += 1
        N = N//K
    else:
        break

print(D)