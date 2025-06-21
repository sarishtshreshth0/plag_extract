x = int(input())
ret = 0
ret += 1000*(x//500)
x = x%500
ret += 5*(x//5)
print(ret)