x = int(input())
happiness = 0

#500円で
happiness += x//500*1000
x %= 500
#5円で
happiness += x//5*5
x %= 5

print(happiness)
