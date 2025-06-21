s= input()

# 0 start
ans1 = 0
for i,c in enumerate(s):
    if i %2==1:
        if c != '1':
            ans1+=1
    else:
        if c !='0':
            ans1+=1

# 1 start
ans2=0
for i,c in enumerate(s):
    if i%2 ==1:
        if c!='0':
            ans2+=1
    else:
        if c!='1':
            ans2+=1

print(min(ans1,ans2))
