n,k = map(int,input().split())

ke = 1
while(True):
    if(n<k):
        print(ke)
        break
    else:
        n = n//k
        ke += 1