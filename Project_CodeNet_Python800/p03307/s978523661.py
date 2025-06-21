n = int(input())
c=n
d=0
for i in range(n, 99999999999999, n):
    if i%2==0 and i%c==0:
        print(i)
        break