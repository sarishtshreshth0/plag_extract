N, A, B = map(int,input().split())
S = input()

temp_num_people = 0
temp_overseas = 0
for s,i in zip(S,range(len(S))):
    if s == 'a':
        if temp_num_people < A+B:
            print('Yes')
            temp_num_people+=1
        else:
            print('No')

    if s == 'b':
        if (temp_num_people < A+B) and (temp_overseas < B):
            print('Yes')
            temp_num_people+=1
            temp_overseas+=1
        else:
            print('No')

    if s == 'c':
        print('No')
