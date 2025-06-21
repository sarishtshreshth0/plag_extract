n,k = map(int,input().split())


keta = 1

while True:
    if n >= k:
        n = n//k
        keta += 1
    else:
        break

print(keta)
