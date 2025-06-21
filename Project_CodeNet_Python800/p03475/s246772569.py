N = int(input())
CC = [0] * (N-1)
SS = [0] * (N-1)
FF = [0] * (N-1)

for i in range(N-1):
    C, S, F = map(int,input().split())
    CC[i] = C
    FF[i] = F
    SS[i] = S

for i in range(N-1):
    T = 0
    Max = 0
    for k in range(i,N-1):
        Max = max(T, SS[k])
        U = Max % FF[k]
        if U == 0:
            T = Max + CC[k]
        else:
            T = Max - U + FF[k] + CC[k]
        #print(i,k,T)
    print(T)
print(0)