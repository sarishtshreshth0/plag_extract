def xor(n):
    num_pair = (n - 1) // 2
    if num_pair % 2 == 0:
        counter = 1
    else:
        counter = 0

    if n % 2 == 0:
        return n ^ counter
    else:
        return counter


a, b = map(int, input().split())

print(xor(b) ^ xor(a - 1))
