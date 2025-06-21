N=int(input())
S=input()
ans1=0
maxans=0
def split(word): 
    return [char for char in word]  
def convert(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 
for i in range(N):
  if S[i]=='(':
    ans1-=1
  else:
    ans1+=1
    if ans1>maxans:
      maxans=ans1
ans2=0
minans=0
for i in range(N):
  if S[N-1-i]==')':
    ans2-=1
  else:
    ans2+=1
    if ans2>minans:
      minans=ans2
r=split(S)
for i in range(minans):
  r.append(')')
r.reverse()
for i in range(maxans):
  r.append('(')
r.reverse()
print(convert(r))