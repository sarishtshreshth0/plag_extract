a,b = map(int,input().split())
s = list(input())
cnt = 0
num = list("0123456789")
for i in range(a):
    if s[i] in num:
        cnt += 1
        
if s[a] == "-":
    cnt += 1
    
for i in range(b):
    if s[i+a+1] in num:
        cnt += 1
        
if cnt == a+b+1:
    print("Yes")
else:
    print("No")