N = int(input())
S = input()

slime = S[0]

for i in range(1, N):
    if S[i] != slime[-1]:
        slime += S[i]

print(len(slime))
