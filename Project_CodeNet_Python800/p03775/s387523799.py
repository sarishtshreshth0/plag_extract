N = int(input())

def f(a, b):
    return len(str(max(a, b)))

res = 100

for i in range(1, int(N**0.5)+1):
    if N%i == 0:
        res = min(f(i, N//i), res)

print(res)