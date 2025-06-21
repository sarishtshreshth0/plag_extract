n=int(input())
a=input()
s=list(a)
b=list(a)
j=0
for i in range(0,n-1):
    if s[i]==s[i+1]:
        b.pop(i-j)
        j=j+1
    else:
        pass
print(len(b))