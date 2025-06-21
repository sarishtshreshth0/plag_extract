S=input()
n=len(S)

a=n
for i in ['01','10']:
 a=min(a,sum(x!=y for x,y in zip(S,(i*(n//2+1))[:n])))
print(a)