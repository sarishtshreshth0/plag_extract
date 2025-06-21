N,A,B = map(int,input().split())
S = input()

pass_num = 0
pass_fo = 0

for i in S:
    if i == 'a':
        if (A + B)-1 >= pass_num:
            print('Yes')
            pass_num += 1
        else:
            print('No')
    elif i == 'b':
        if ((A+B-1) >= pass_num)and(pass_fo <= B-1):
            print('Yes')
            pass_num += 1
            pass_fo += 1
        else:
            print('No')
    else:# i == 'c'
        print('No')