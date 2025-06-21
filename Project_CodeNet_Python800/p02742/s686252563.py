h,w=map(int,input().split())

if h==1 or w==1:
    print(1)
elif h%2==0:
    print(h//2*w)
elif w%2==0:
    print(w//2*h)
else:
    print(h*((w-1)//2)+(h+1)//2)
