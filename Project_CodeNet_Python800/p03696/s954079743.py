n=int(input())
s=input()
a=[1 if i=='(' else -1 for i in s]
e=[0]
for i in range(n):
    e.append(e[i]+a[i])
s=-min(e)*'('+s
s+=(s.count('(')-s.count(')'))*')'
print(s)
#print(e)