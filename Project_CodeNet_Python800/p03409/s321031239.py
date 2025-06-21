n=int(input())

red=[]
for _ in range(n):
  a,b=map(int,input().split())
  red.append((a,b))

blue=[]
for _ in range(n):
  c,d=map(int,input().split())
  blue.append((c,d))

blue.sort()
red.sort()
cnt=0

#print(blue,red)

for item1 in blue:
  x,y=item1[0],item1[1]
  result=[]
  for item2 in red:
    xx,yy=item2[0],item2[1]
    if x>xx and y>yy:
      if result==[]:
        result=[xx,yy]
      else:
        if yy>result[1]:
          result=[xx,yy]
  if result!=[]:
    #print(x,y,result)
    red.remove((result[0],result[1]))
    cnt+=1
print(cnt)


        
        
    
  


  
