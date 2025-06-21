import math

n = int(input())

def f(a, b):
    x = int(max(a, b))
    return len(str(x))

results = []

# itr_end = int(n ** 0.5) + 1
itr_end = int(math.sqrt(n)) + 1

for i in range(1, itr_end):
    if n % i == 0:
        a = i
        b = n / i
    result = f(a, b)
    results.append(result)

print(min(results))

