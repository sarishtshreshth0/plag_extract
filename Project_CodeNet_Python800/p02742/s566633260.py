f=lambda h,w:((h+1)//2)*((w+1)//2)+(h//2)*(w//2)
h, w = map(int, input().split())
print(1 if h==1 or w==1 else f(h, w))
