n=int(input())
s=input()
a=[s[0]]
for i in range(1,n):
  if s[i]!=s[i-1]:
    a.append(s[i])
"".join(a)
print(len(a))