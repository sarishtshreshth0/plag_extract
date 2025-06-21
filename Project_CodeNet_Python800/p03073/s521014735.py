S = input()

if S[0]=="0":
  ans = ["0","1"]*(10**5//2)
    
else:
  ans = ["1","0"]*(10**5//2)

count = 0
for i in range(len(S)):
  if S[i]!=ans[i]:
    count+=1
print(count)