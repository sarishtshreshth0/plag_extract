a,b = map(int, input().split())
num = [2,3,4,5,6,7,8,9,10,11,12,13,1]
for i in range(1,14):
    if a == i:
        x = num.index(a)
    if b == i:
        y = num.index(b)
if x < y:
    print('Bob')
elif x > y:
    print('Alice')
else:
    print('Draw')