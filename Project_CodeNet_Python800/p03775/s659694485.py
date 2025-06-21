n = int(input())

fab = 0

ans = 1000

n_s = int(n ** (1/2))

for i in range(1, n_s + 2):
    if n % i == 0:
        a = len(str(i))
        b = len(str(int(n / i)))
        #print(n/i, i, a, b)
        if a > b and a < ans:
            ans = a
        elif a < b and b < ans:
            ans = b
        elif a == b and a < ans:
            ans = a


print(ans)