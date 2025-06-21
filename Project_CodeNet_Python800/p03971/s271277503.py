n,a,b=map(int,input().split())
s=input()

count_ab=0
count_b=0

for i in range(n):
    if s[i]=='c':
        print('No')
    elif s[i]=='a':
        if count_ab<a+b:
            print('Yes')
            count_ab+=1
        else:
            print('No')
    elif s[i]=='b':
            if count_b<b and count_ab<a+b:
                print('Yes')
                count_b+=1
                count_ab+=1
            else:
                print('No')
    else:
        print('No')