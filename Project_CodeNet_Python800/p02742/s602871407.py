h, w = map(int, input().split())

if h == 1 or w == 1:
    print(1)
else:
    odd = ((h + 1)//2)  * ((w + 1)//2)
    even = (h//2) * (w//2)
    print(odd + even)