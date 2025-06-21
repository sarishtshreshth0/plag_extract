S = input()
N = len(S)

count1 = 0
count2 = 0
for i in range(N):
    ex = str(i % 2)
    if S[i] == ex:
        count1 += 1
    else:
        count2 += 1
print(min(count1, count2))