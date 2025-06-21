N = int(input())
C, S, F = zip(*(tuple(map(int, input().split())) for _ in range(N - 1)))
for i in range(N - 1):
    total = S[i] + C[i]
    for j in range(i + 1, N - 1):
        if total <= S[j]:
            total = S[j]
        else:
            div, rem = divmod(total, F[j])
            total = (div + bool(rem)) * F[j]
        total += C[j]
    print(total)
print(0)