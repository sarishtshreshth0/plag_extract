n,k = map(int,input().split())
digits = 0
while True:
    if n >= k**digits:
        digits += 1
    else:
        print(digits)
        exit()