n=int(input())
s=list(input())

for x in range(n-1):
  if s[x]==s[x+1]:
    s[x]='1'
    
print(len(s)-s.count('1'))