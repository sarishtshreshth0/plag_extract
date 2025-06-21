h,w = map(int, raw_input().split(' '))
def f(h,w): return 1 if h == 1 or w == 1 else (h - (h/2)) * ((w - w/2)) + ((h/2)) * (w/2)
print f(h,w)