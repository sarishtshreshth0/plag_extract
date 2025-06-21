s=input()

c1=0
c2=0

for i in range(len(s)):
    if i%2==0:
        c1+=1 if s[i]=='1' else 0
        c2+=1 if s[i]=='0' else 0
    else:
        c1+=1 if s[i]=='0' else 0
        c2+=1 if s[i]=='1' else 0
    
print(min(c1,c2))