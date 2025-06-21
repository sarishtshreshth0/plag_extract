N=int(input())
S=list(input())
#print(S)

S_orig=list(S)
while True:
  update=False
  
  remove_flg=[False]*len(S)
  for i in range(1,len(S)):
    if S[i-1]=='(' and S[i]==')':
      remove_flg[i-1]=remove_flg[i]=True
      update=True      
  if not update:
    break
      
  new_S=[]
  for i in range(len(S)):
    if not remove_flg[i]:
      new_S.append(S[i])      
  S=new_S
  
cnt_l=cnt_r=0
for i in range(len(S)):
  if S[i]=='(':
    break
  else:
    cnt_l+=1
for i in reversed(range(len(S))):
  if S[i]==')':
    break
  else:
    cnt_r+=1
#print(cnt_l,cnt_r)

answer_S=['(']*cnt_l+S_orig+[')']*cnt_r
print("".join(answer_S))