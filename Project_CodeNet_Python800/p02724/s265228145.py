n = int(input())
res = 0
a = n // 500
n %= 500
b = n // 5
print(1000*a + 5*b)