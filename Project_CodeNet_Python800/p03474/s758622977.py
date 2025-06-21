l,m=map(int,input().split())
p=input().split("-")
print('NYoe s'[len(p)==2 and len(p[0])==l and len(p[1])==m::2])