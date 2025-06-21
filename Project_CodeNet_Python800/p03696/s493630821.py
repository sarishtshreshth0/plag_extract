input()
t=s=input()
p,q=o="()"
while o in s:s=s.replace(o,"")
f=s.count
print(p*f(q)+t+q*f(p))	