N=int(input())

def ans(N):
    if N%2 == 0:
        return N
    else:
        return N*2
        
print(ans(N))