# B - Qualification simulator

N, A, B = map(int, input().split())
S = list(str(input()))

total = 0
total_B = 0
for s in S:
    if s == 'a' and total < (A + B):
        total += 1
        print('Yes')
    elif s == 'b' and total < (A + B) and total_B < B:
        total += 1
        total_B += 1
        print('Yes')
    else:
        print('No')     