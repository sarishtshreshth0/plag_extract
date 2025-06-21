a, b = map(int, input().split())
def f(n):
    if n % 2:
        return 1 if -(-n//2) % 2 else 0
    else:
        return 1 + n if (n//2) % 2 else n 
print(f(a - 1) ^ f(b))