money = int(input())

gohyakuen = money // 500

goen = (money-(gohyakuen*500)) // 5

happy = 1000 * gohyakuen + 5 * goen

print(happy)
