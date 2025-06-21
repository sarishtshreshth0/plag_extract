score = list(map(int,input().split()))
keta = 0
answer = 1
while score[0] >= answer:
    answer *= score[1]
    keta += 1
print(keta)