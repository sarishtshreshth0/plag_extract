h, w = map(int,input().split())
print((h*w+1)//2 if h!=1 and w!=1 else 1)