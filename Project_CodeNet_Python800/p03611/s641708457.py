N = int(input())
a = list(map(int, input().split()))
A = [0] * (10 ** 5 + 5)
for ai in a:
    A[ai - 1] += 1
    A[ai] += 1
    A[ai + 1] += 1
print(max(A))