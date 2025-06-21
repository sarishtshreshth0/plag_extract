h,w = map(int, input().split())

if h==1 or w == 1:
    print(1)
    exit()
if w%2==0: a = w//2
else: a = w//2+1

print(w*(h//2) if h%2==0 else w*(h//2)+a)