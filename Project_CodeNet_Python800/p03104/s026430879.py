A, B = map(int, input().split())
A -= 1


def calc(n):
    if n % 2 == 1:
        if (n + 1) % 4 == 0:
            return 0
        else:
            return 1
    else:
        return calc(n-1) ^ n


print(calc(B) ^ calc(A))

