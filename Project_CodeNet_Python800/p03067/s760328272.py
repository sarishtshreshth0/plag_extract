a,b,c=map(int,input().split())
f= a<=c<=b or b<=c<=a
print("Yes" if f==True else "No")