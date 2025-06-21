def koubaisu(N,M):
    NM = N*M
    if M>N:
        N,M = M,N
    while(N%M!=0):
        Temp = N
        N = M
        M = Temp%M
    return NM//M
N = int(input())
print(koubaisu(N,2))