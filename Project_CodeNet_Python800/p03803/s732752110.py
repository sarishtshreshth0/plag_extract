card = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
alice, bob = map(int, input().split())
if card.index(alice) > card.index(bob):
    print('Alice')
elif card.index(alice) < card.index(bob):
    print('Bob')
else:
    print('Draw')
