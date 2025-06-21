x = int(input())
ans = (x // 500) * 1000
x -= (x // 500) * 500
print(ans+(x//5)*5)

