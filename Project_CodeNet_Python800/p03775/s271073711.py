n = int(input())

def f(a, b):
    x = int(max(a, b))
    return len(str(x))

results = []

for i in range(1, int(n ** (1/2)) + 1):
    if n % i == 0:
        a = i
        b = n / i
    result = f(a, b)
    results.append(result)

print(min(results))