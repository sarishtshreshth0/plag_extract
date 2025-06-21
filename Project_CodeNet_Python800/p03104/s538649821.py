A,B = map(int,(input().split()))
def xor(n):
    if n%2 == 1:
        if (n+1)%4 == 0:
            return 0
        else:
            return 1
    else:
        if n%4 == 0:
            return n^0
        else:
            return n^1
            
print(xor(A-1)^xor(B))