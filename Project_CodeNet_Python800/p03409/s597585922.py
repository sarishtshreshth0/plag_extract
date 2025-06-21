N=int(input())

red_list=[]
for i in range(N):
  a,b=map(int,input().split())
  red_list.append((a,b))
red_list.sort()
  
blue_list=[]
for i in range(N):
  c,d=map(int,input().split())
  blue_list.append((c,d))
blue_list.sort()

#print(red_list)
#print(blue_list)

answer=0
selected_set=set()
for i in range(N):
  c,d=blue_list[i]
  max_y=-1
  maxarg_y=-1
  for j in range(N):
    a,b=red_list[j]
    if c<=a:
      break
    
    if b<d and b>max_y and not j in selected_set:
      max_y=b
      maxarg_y=j
      
  if maxarg_y!=-1:
    answer+=1    
    selected_set.add(maxarg_y)
    #print(red_list[maxarg_y],blue_list[i])
    
print(answer)
