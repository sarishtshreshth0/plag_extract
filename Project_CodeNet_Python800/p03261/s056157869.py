n=int(input())
check=[]
s=input()
check.append(s)
ans=0
for i in range(n-1):
  keep=s[-1]
  s=input()
  if keep != s[0]:
    ans=1
  if str(s) in check:
    ans = 1
  else:
    check.append(s)
print(["Yes","No"][ans])