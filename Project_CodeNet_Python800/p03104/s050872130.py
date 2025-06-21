# D - XOR World

A, B = map(int, input().split())

def rangeXOR(x, y):
    ret = x
    for i in range(x+1, y+1):
        ret ^= i
    return ret

left = rangeXOR(A, A+(3-A%4))
right = rangeXOR(B-(B%4), B)
    
if left==0:
    print(right)
elif right==0:
    print(left)
else:
    print(left^right)