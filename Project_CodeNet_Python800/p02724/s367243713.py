x = int(input())

n_500 = int(x / 500)
h = 1000 * n_500
x -= 500 * n_500

n_5 = int(x / 5)
h += 5 * n_5

print(int(h))
