n=int(input())
s=input()
c=s[0]
for i in range(1,n):
    if s[i]!=s[i-1]:
        c=c+s[i]
print(len(c))
