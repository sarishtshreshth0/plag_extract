H,W=map(int,input().split())

w1=0--W//2
w2=W//2

if H==1 or W==1:
    print(1)
else:
    print(w1*(0--H//2)+w2*(H//2))