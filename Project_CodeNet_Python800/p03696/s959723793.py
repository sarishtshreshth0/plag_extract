n=int(input())
s=input()

left=0
right=0
for s_i in s:
    if s_i=='(':
        right+=1
    elif s_i==')':
        if right>0:
            right-=1
        else:
            left+=1

print('('*left+s+')'*right)


