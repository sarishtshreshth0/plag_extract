h,w=map(int,input().split())
print((h*w+1)//2 if h*w>h+w else 1)