A, B = map(int, input().split())
ans = 0

def f(n):
    # F(0, n)
    if n % 2 == 0:
        if (n//2) % 2 == 0:
            return 0^n
        else:
            return 1^n
    else:
        if ((n+1)//2) % 2 == 0:
            return 0
        else:
            return 1

print(f(A-1)^f(B))