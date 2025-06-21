a1,a2,b1,b2 = map(int,input().split())
a1,a2,b1,b2
count = 0
if a1 <= b1:
    for i in range(a2+1):       
        if i > b1 and i <= b2:
            count += 1
elif b1 <= a1:
    for i in range(b2+1):
        if i > a1 and i <= a2:
            count += 1
print(count)