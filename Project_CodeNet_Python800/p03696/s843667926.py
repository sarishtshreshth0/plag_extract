n=int(input())
s=list(input())
cnt=0
right=0
left=0
for i in range(len(s)):
    if s[i] == '(':
        cnt+=1
    else:
        cnt-=1
    if cnt < 0:
        right+=1
        cnt=0
if cnt>0:
    left=cnt
for i in range(right):
    s.insert(0,'(')
for i in range(left):
    s.append(')')
print(''.join(s))