n,a,b = map(int,input().split())
s = list(input())
cap = a+b

for i in s:
    if i == 'a' and cap > 0:
        print('Yes')
        cap -= 1
    elif i == 'b' and cap > 0 and b > 0:
        print('Yes')
        cap -= 1
        b -= 1
    else:
        print('No')
        
