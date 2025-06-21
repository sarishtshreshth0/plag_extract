h,w=map(int,input().split())
if (h-1)*(w-1)==0:
    print(1)
else:
    print((h*w)//2 if (h*w)%2==0 else (h*(w-1))//2+(h+1)//2)