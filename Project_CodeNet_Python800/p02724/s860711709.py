X = int(input())
gohyaku,X = divmod(X,500)
go,X = divmod(X,5)
print(1000*gohyaku+5*go)