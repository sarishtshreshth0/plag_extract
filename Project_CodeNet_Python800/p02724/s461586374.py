x = int(input())

r = 0
divider = ((500,1000), (5, 5))
for i in divider:
    x, remain = divmod(x, i[0])
    r += x * i[1]
    x = remain

print(r)