
n = int(input())

s = input()

now =0
right = 0
for i in range(n):
    if(s[n-1-i]=='('):
        now+=1
    else:
        now-=1
    if(right<now):
        right=now
left=0
now=0
for i in range(n):
    if(s[i]=='('):
        now-=1
    else:
        now+=1
    if(left<now):
        left=now

print('('*left +s+ ')'*right)