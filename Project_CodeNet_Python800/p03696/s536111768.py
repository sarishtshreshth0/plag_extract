n = int(input())
s = input()
l=0
r=0
for i in s:
    if i ==')' and l==0:
        r+=1
    elif i==')':
        l-=1
    elif i=='(':
        l+=1
s1 = '('*r
s2 = ')'*l
s=s1+s+s2
print(s)
