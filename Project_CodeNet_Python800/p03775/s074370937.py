n = int(input())
m = int(n**0.5)

while n%m:
    m -= 1

print(len(str(n//m)))