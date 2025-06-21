x = int(input())
yen_500 = 0
yen_5 = 0
amari = 0
happy = 0

if x>= 500:
    yen_500 = x//500
    amari = x - 500 * yen_500
    yen_5 = amari//5
    happy = 1000 * yen_500 + 5 * yen_5
    print(happy)
else:
    yen_5 = x//5
    happy = 5 * yen_5
    print(happy)
