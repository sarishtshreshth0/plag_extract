n = int(input())
c = n // 500
d = n % 500
print(1000 * c + 5 * (d // 5))