Alice, Bob = map(lambda x: int(x) * 100 if x ==
                 '1' else int(x), input().split(' '))

if Alice == Bob:
    print('Draw')
elif Alice > Bob:
    print('Alice')
else:
    print('Bob')
