x=int(input())
num=x//500
ans=1000*num
x-=500*num
ans+=5*(x//5)
print(ans)