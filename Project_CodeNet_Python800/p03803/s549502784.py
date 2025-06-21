a, b = map(int, input().split())
point = [13,1,2,3,4,5,6,7,8,9,10,11,12]
alice = point[a-1]
bob = point[b-1]
if alice > bob:
    print('Alice')
elif alice < bob:
    print('Bob')
else:
    print('Draw')
