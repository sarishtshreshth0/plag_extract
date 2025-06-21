def xor_0_n(n):
    if n % 2 == 1 and (n//2) % 2 == 1:
        n = 0
    elif n % 2 == 1 and (n//2) % 2 == 0:
        n = 1
    elif n % 2 == 0 and (n//2) % 2 == 1:
        n ^= 1
    return n
  
a, b = map(int,input().split())

print(xor_0_n(a-1)^xor_0_n(b))
