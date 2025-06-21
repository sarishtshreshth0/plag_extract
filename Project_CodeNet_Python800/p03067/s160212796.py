a,b,c = map(int,input().split())
print("Yes" if (a<b and a<c<b) or (a>b and b<c<a) else "No")