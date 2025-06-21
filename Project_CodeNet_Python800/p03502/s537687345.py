def f(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

N = int(input())

if N % f(N) == 0:
    print("Yes")
else:
    print("No")
