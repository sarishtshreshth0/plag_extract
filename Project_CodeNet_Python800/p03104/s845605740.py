A, B = map(int, input().split())


def f(n):
    if n % 2:
        return (n + 1) // 2 % 2
    else:
        return n // 2 % 2 ^ n


ans = f(A - 1) ^ f(B)
print(ans)

# F(A, B) = F(0, A - 1) ⊕ F(0, B)
# f(n) = F(0, n)
#  任意の偶数nについて n ⊕ (n + 1) = 1
# 0 ⊕ 1 ⊕ 2 ⊕ 3 ⊕ 4 ⊕ 5 ⊕ 6
# = (0 ⊕ 1) ⊕ (2 ⊕ 3) ⊕ (4 ⊕ 5) ⊕ 6
# = 1 ⊕ 1 ⊕ 1 ⊕ 6
