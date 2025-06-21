n=int(input())
s=input()
a=[]
for i in range(n):
    if i==n-1:
        a.append(s[i])
        continue
    if s[i]!=s[i+1]:
        a.append(s[i])
print(len(a))