import math
n = int(input())
m = math.floor(math.sqrt(n))
for i in range(1,m+1):
    if n % i == 0:
        x = i
y = n // x
print(max(len(str(x)),len(str(y))))