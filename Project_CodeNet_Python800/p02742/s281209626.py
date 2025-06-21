h,w = map(int,input().split())
t = w//2+(w%2!=0)
ans  = (t+w//2)*(h//2)+t*(h%2!=0)
if h == 1 or w == 1:
    print(1)
    exit()
print(ans)