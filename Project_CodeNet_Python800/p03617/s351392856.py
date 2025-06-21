Q, H, S, D = map(int, input().split())
N = int(input())
kouho = []
mv = int(1e9)

if N % 2 == 0:
    for i, j in zip([Q, H, S, D], [0.25, 0.5, 1, 2]):
        kouho.append(int((N // j)*i))
else:
    for i, j in zip([Q, H, S, D], [0.25, 0.5, 1, 2]):
        kouho.append(int((N // j)*i))

    for i, j in zip([Q, H, S], [0.25, 0.5, 1]):
        mv = int(min(i // j, mv))
    kouho[-1] += mv
print(min(kouho))
