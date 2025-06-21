def xor_array(n):
    if (n + 1) % 4 == 0:
        return 0
    elif (n + 1) % 2 == 0:
        return 1
    elif n % 4 == 0:
        return n
    else:
        return 1 ^ n


a, b = map(int, input().split())
print(xor_array(a - 1) ^ xor_array(b))
