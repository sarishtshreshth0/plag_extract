X=int(input())
q,mod=divmod(X,500)
p=mod//5
print(q*1000+p*5)