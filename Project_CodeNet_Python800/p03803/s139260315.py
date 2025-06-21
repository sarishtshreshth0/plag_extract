alice, bob = map(int, input().split())
if alice == 1 and bob != 1:
    print('Alice')
elif alice != 1 and bob == 1:
    print('Bob')
elif alice == bob:
    print('Draw')
else:
    if alice < bob:
        print('Bob')
    else:
        print('Alice')