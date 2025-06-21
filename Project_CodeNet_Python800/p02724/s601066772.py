x = int(input())

yen_500 = x//500
yen_5 = (x-(yen_500*500))//5

print((yen_500*1000)+(yen_5*5))
