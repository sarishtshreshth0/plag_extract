def get_xor_product(n):
    ans = 0
    if n % 2:
        ans = ((n + 1) // 2) % 2
    else:
        ans = (n // 2) % 2
        ans ^= n
    return ans


A, B = map(int, input().split())
ans = get_xor_product(A - 1) ^ get_xor_product(B)
print(ans)
