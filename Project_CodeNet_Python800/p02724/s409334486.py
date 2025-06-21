x=int(input())

A=int(x//500)
B=int((x%500)//5)

ans=0
ans=A*1000+B*5
print(ans)