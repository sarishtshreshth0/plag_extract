#B - Qualification simulator
N,A,B = map(int,input().split())
S = input()
S = list(S)

capacity = A + B
candidate = 0
overseas = 0
for i in S:
    if i == 'a' and candidate < capacity:
        candidate += 1
        print('Yes')
    elif i == 'b' and candidate < capacity and overseas < B:
        candidate += 1
        overseas += 1
        print('Yes')
    else :
        print('No')