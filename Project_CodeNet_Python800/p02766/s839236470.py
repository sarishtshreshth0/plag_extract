n, k = map(int,input().split())
b = ''
while n > 0:
    b += str(n % k)
    n = n // k
print(len(b))
