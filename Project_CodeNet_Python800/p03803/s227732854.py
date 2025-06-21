a,b = map(int, input().split())
powers = list(range(2,13+1))+[1]
if powers.index(a) > powers.index(b):
    print('Alice')
elif powers.index(b) > powers.index(a):
    print('Bob')
else:
    print('Draw')