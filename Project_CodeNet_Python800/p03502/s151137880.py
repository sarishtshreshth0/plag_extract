s=input()
t_sum=0
for ss in s:
  t_sum+=int(ss)
if int(s)%t_sum==0:
  print("Yes")
else:
  print("No")