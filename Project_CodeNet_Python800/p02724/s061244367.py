X=int(input())
ans=1000*(X//500)+5*((X-(X//500*500))//5)
print(ans)