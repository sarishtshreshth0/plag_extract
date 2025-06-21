N , K = map(int, input().split())

for x in reversed(range(0,30)):
    if N/(K**x) >= 1:
        print(x+1)
        break