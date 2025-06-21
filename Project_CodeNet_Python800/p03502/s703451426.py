s = input()
n = int(s)

answer = False
x = n

h = []
while (x > 0):
    h.append(x % 10)
    x = int(x / 10)



f = 0

for i in range(len(h)):
    f += h[i]

if n % f == 0:
    answer = True

if answer:
    print('Yes')
else:
    print('No')