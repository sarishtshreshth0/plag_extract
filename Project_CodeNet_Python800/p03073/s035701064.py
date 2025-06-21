s=input()
n=len(s)

x=[i%2 for i in range(n)]
y=[(i+1)%2 for i in range(n)]
d=0
f=0

for i in range(n):
    if int(s[i])!=x[i]:
        d+=1
for i in range(n):
    if int(s[i])!=y[i]:
        f+=1
print(min(d,f))
