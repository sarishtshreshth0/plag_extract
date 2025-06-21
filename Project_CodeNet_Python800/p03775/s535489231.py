N = int(input())

a = len(str(N))
i = 1
while i*i <= N:
    if N % i == 0:
        a = min(a, len(str(N//i)))
    i += 1

print(a)
