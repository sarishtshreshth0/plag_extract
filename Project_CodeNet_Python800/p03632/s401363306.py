a,b,c,d=map(int,input().split())

s=max(a,c)
f=min(b,d)
print(max(f-s,0))