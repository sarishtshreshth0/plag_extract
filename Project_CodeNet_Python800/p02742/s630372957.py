import sys
h,w=map(int,input().split())
if h==1 or w==1:
    print(1)
    sys.exit()
if h%2==0 and w%2==0:
    print(int(h*w/2))
elif h%2==1 and w%2==1:
    print(int(h*w/2)+1)
else:
    print(int(h*w/2))