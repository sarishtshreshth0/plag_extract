N, A, B = map(int, input().split())
S = input()

capacity = A+B
rank = 1
for i in range(N):
    if 'a' == S[i] and 0 < capacity:
        print('Yes')
        capacity -= 1
    elif 'b' == S[i] and 0 < capacity and rank <= B:
        print('Yes')
        capacity -= 1
        rank += 1
    else:
        print('No')
