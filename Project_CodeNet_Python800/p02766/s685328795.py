c = 0
n, b = map(int, input().split())
while n > 0:
    c +=1
    n//=b
print(c)