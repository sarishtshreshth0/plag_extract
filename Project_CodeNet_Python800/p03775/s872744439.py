import math
n = int(input())
root_n = int(math.sqrt(n)) + 10
ans = 1<<60
def f(a, b):
    len_a = len(str(a))
    len_b = len(str(b))
    return max(len_a, len_b)
for i in range(1, root_n):
    if n % i == 0:
         ans = min(ans, f(i, n // i))
print(ans)