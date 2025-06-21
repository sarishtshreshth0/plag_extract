n=int(input())
k=n//500
n -= k*500
n //= 5
print(k*1000+n*5)