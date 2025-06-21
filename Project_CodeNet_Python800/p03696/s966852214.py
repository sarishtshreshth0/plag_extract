N=int(input())
S=input()

add_left=0
add_right=0
for s in S:
  if s=="(":
    add_right+=1
  elif add_right==0:
    add_left+=1
  else:
    add_right-=1

print('(' * add_left + S + ')' * add_right)
