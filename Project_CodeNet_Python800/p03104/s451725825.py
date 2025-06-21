
A, B = map(int, input().split())

A -= 1

if (A+1) % 2 == 0:
    a = (A+1) // 2 % 2
else:
    a = (A // 2 % 2) ^ A

if (B+1) % 2 == 0:
    b = (B+1) // 2 % 2
else:
    b = (B // 2 % 2) ^ B
    
#print(a, b)
print(a ^ b)