def actual(n):
    if n % 2 == 0:
        return n

    return 2 * n

n = int(input())
print(actual(n))