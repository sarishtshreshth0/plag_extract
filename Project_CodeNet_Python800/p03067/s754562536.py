h = list(map(int,input().split()))
if h[0]<h[2] and h[2]<h[1]:
    print("Yes")
elif h[1]<h[2] and h[2]<h[0]:
    print("Yes")
else:  
    print("No")