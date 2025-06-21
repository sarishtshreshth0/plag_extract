input()
s=t=input()
p,q=o="()"
exec('s=s.replace(o,"");'*50)
f=s.count
print(p*f(q)+t+q*f(p))