a=int(input())
b=a//500
ans=b*1000+((a-b*500)//5)*5
print(ans)