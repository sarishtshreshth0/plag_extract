n = int(input())
l = list(map(int,input().split(" ")))
total = 0
for i in l:
    total += i

x = l[0]
y = total - x
a = abs(x - y)


for t in range(n):
    x = 0
    for i in range(t+1):
        x += l[i]
    y = total - x
    b = abs(x - y)
    if a > b:
        a = b

print(a)