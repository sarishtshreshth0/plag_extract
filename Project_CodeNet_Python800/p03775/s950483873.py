n = int(input())

ans = 1
for i in range(2, 10 ** 5):
    if n % i == 0:
        ans = i
    if i * i > n:
        break

print(len(str(n // ans)))