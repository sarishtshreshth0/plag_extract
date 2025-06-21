a,b=map(int,input().split())
a-=1
a+=((a+1)//2)%2-(a%2)*a
b+=((b+1)//2)%2-(b%2)*b
print(a^b)