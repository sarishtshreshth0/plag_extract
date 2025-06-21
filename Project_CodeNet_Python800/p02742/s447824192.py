h,w=map(int,input().split())
ans=0
if h==1 or w==1:
    ans=1
elif (h*w)%2==0:
    ans=int(h*w//2)
else:
    ans=(h*w//2+1)
print(ans)