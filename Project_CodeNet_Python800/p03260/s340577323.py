a,b = map(int,input().split())

for c in range(1,4):
    s = a * b * c
    if s % 2 != 0:
        print('Yes')
        break
    
else:
    print('No')