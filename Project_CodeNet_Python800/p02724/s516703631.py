# B - Golden Coins

# X
X = int(input())

kiri_happy = X // 500
inaho_happy = (X - (500 * kiri_happy)) // 5

answer = (kiri_happy * 1000) + (inaho_happy * 5)

print(answer)
