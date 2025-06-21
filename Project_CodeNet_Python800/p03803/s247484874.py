cards = input()
cards_s = cards.split()

porker_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '1']

alice_str = cards_s[0]
alice_s = porker_list.index(alice_str)
alice = int(alice_s)

bob_str = cards_s[1]
bob_s = porker_list.index(bob_str)
bob = int(bob_s)

if alice > bob:
    print('Alice')
elif alice == bob:
    print('Draw')
else:
    print('Bob')
