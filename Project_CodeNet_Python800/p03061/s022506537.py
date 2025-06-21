from math import gcd

n = int(input())
A = list(map(int, input().split()))

if n == 2:
    print(max(A))
else:
    # 最初の3個のうちの2個を選んで、最大の最大公約数
    # 最大公約数に選ばれなかったものを交換（rがaより大きいとき）
    r = max(gcd(A[0], A[1]), gcd(A[1], A[2]), gcd(A[2], A[0]))
    # リストaの最初3個の最大公約数
    a = gcd(A[0], gcd(A[1], A[2]))

    for i in range(3, n):
        r = max(gcd(A[i], r), a)
        a = gcd(A[i], a)

    print(r)