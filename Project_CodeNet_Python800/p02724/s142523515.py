X = int(input())

gohyaku = X // 500
X = X - (gohyaku * 500)
goen = X // 5

print(gohyaku * 1000 + goen * 5)