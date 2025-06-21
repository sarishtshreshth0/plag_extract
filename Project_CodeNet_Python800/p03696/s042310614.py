n=int(input())
s=input()
left=0
left_cnt=0
for i in s:
    if i=="(":
        left+=1
    else:
        if left>=1:
            left-=1
        else:
            left_cnt+=1
right=0
right_cnt=0
for i in s[::-1]:
    if i==")":
        right+=1
    else:
        if right>=1:
            right-=1
        else:
            right_cnt+=1
print("("*left_cnt+s+")"*right_cnt)