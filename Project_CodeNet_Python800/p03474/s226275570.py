a,b=map(int,input().split())
s=input()
if s.count('-')!=1:
	r='No'
else:
	t,u=s.split('-')
	if len(t)==a and len(u)==b and (t+u).isdecimal():
		r='Yes'
	else:
		r='No'
print(r)