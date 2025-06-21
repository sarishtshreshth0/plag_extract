x = input()
if int(x) % sum(map(int, x)) == 0:
    print('Yes')
else:
    print('No')