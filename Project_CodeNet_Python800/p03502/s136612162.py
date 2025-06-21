N = int(input())
n = N
t = 0

while n > 0 :
    t += n % 10
    n //= 10

print("Yes" if N%t == 0 else "No")