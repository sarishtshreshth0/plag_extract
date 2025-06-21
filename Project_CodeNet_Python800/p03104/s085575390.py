a, b = map(int, input().split())

def F(n):
    a = n//2
    if n % 2 == 0:
        if a % 2 == 0:
            return n
        else:
            return n ^ 1
    else:
        if a % 2 == 0:
            return 1
        else:
            return 0

ans = F(a-1) ^ F(b)
print(ans)
