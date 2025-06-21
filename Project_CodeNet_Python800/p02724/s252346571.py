x = int(input())

n_500 = x//500
n_5 = (x%500)//5

print(n_500*1000 + n_5*5)