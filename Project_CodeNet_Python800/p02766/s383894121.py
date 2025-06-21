N,K = (int(x) for x in input().split())
Conv = []
while N!=0:
    Conv.append(N%K)
    N = N//K
    
Disp = ''.join([str(x) for x in Conv[::-1]])
print(len(Disp))