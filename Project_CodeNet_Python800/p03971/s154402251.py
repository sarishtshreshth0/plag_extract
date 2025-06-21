n, a, b=map(int, input().split())
s=str(input())
cnt_a=0
cnt_b=0
for i in range(len(s)):
    if s[i]=='c':
        print('No')
    if s[i]=='a':
        if cnt_a+cnt_b<a+b:
            cnt_a+=1
            print('Yes')
        else:
            print('No')
    if s[i]=='b':
        if cnt_a+cnt_b<a+b and cnt_b<b:
            cnt_b+=1
            print('Yes')
        else:
            print('No')
        
    
    
