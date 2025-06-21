def f(x):
    res = (x+1)//2%2
    
    for i in range(1, 50):
        n = x%2**(i+1)
        
        if n>=2**i and (n-2**i)%2==0:
            res += 2**i
    
    return res

A, B = map(int, input().split())

if A==0:
    print(f(B))
else:
    print(f(B)^f(A-1))
