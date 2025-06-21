x = int(input())

five_hand = 500
five = 5
glad = 0

if x >= five_hand:
    glad = glad + (x // five_hand) * 1000
    x = x % five_hand

if x >= five:
    glad = glad + (x // five) * 5
    x = x % five

print(glad)