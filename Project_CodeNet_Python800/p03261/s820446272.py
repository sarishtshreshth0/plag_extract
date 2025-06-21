N = int(input())
W = [input() for _ in range(N)]

if len(set(W)) != len(W):
    print("No")
    exit()

prev = W[0][0]
for w in W:
    if w[0] != prev:
        print("No")
        exit()
    prev = w[-1]
print("Yes")