A, B = map(int, input().split())
xorA = [0] * 41
xorB = [0] * 41
def xor_list(l, N):
    k = 1
    while 2 ** k // 2 <= N:
        tmp = (N+1) % (2 ** k)
        if k == 1:
            l[k-1] = (N+1) // (2 ** k)
            k += 1
        elif tmp <= 2 ** k // 2:
            k += 1
            continue
        else:
            l[k-1] = (tmp - 2 ** k // 2) % 2
            k += 1
        if k == 1:
            count = (N + 1) // (2 ** k) + tmp + 1
            l[0] = (count % 2)
xor_list(xorA, A-1)
xor_list(xorB, B)
ans = 0
for i in range(41):
    ans += abs(xorA[i] - xorB[i]) % 2 * (2 ** i)
print(ans)