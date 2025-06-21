N, A, B = list(map(int, input().split()))
S = input()

count_A = 0
count_B = 0
for i in range(N):
    if S[i] == 'c':
        print('No')
    elif S[i] == 'a':
        count_A += 1
        if count_A + count_B <= A + B:
            print('Yes')
        else:
            print('No')
            count_A -= 1
    elif S[i] == 'b':
        count_B += 1
        if count_A + count_B <= A + B and count_B <= B:
            print('Yes')
        else:
            print('No')
            count_B -= 1