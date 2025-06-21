a,b,c=map(int,input().split())
print(("No","Yes")[(a-c)*(c-b)>0])