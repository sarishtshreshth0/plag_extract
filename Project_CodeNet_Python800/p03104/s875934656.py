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
a,b=map(int,input().split())
ans=[]
abin="{0:b}".format(a)
bbin="{0:b}".format(b)
abin=split(abin)
bbin=split(bbin)
abin.reverse()
bbin.reverse()
for i in range(len(bbin)-len(abin)):
  abin.append('0')
if (abin[0]=='1' and ((b-a)%4==0 or (b-a)%4==1)) or (abin[0]=='0' and ((b-a)%4==1 or (b-a)%4==2)) :
  ans.append('1')
else:
  ans.append('0')
for i in range(1,len(bbin)):
  flag=0
  if abin[i]=='1' and a%2==1:
    flag+=1
  if bbin[i]=='1' and b%2==0:
    flag+=1
  if flag==1:
    ans.append('1')
  else:
    ans.append('0')
ans.reverse()
print(int(convert(ans),2))