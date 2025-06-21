a, b = map(int, input().split())
def f(n):
    if n % 2:
        return -(-n//2) % 2
    else:
        return (n//2) % 2 + n
print(f(a - 1) ^ f(b))