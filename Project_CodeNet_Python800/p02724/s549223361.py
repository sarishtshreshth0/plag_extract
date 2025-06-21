N = int(input())
d = N // 500
mod = N % 500
d2 = mod // 5
print(d*1000+d2*5)