s=list(input().split())
if int(s[0])<int(s[2])<int(s[1]):
        c='Yes'
elif int(s[1])<int(s[2])<int(s[0]):
        c='Yes'
else:
        c='No' 
print(c)