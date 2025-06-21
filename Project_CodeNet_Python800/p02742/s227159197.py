a, b = map(int,input().split())
n = a*b
if a == 1 or b == 1:
    print(1)
    exit()
elif n % 2 == 0:
    print(n // 2)
    exit()
    
else:
    print((n + 1) // 2)