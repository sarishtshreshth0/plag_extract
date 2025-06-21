import math
N,K=map(int,input().split())

if(N==1):
    print(1)
    exit()
print(math.ceil(math.log(N,K)))
