n = int(input())

start = int(n**0.5 + 1)
for a in range(start,0,-1):
    if n%a == 0:
        b = n//a
        print(len(str(b)))
        exit()