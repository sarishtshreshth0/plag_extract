x = int(input())

a = x // 500
b = x % 500 // 5
ans = 1000*a + 5*b
print(ans)