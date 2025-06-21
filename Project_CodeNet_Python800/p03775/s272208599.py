n = int(input())
nn = int(n**(1/2))
while True:
    if n % nn == 0:
        break
    nn -= 1
print(len(str(n//nn)))