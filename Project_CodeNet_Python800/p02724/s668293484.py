x = int(input())
d = x // 500
v = (x % 500) // 5 
print(d * 1000 + v * 5)