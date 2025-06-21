S=input()
chars = []
moves1 = 0
moves2 = 0
n = 0
for c in S:
    n += 1
    if c == '0':
        if n % 2 == 0:
            moves1 += 1
        else:
            moves2 += 1
    else:
        if n % 2 == 0:
            moves2 += 1
        else:
            moves1 += 1

print(min(moves1,moves2))

