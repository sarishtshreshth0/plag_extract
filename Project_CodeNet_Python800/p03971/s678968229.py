"""
CODE FESTIVAL 2016
"""
N,A,B = map(int,input().split())
S = input()
sum_a = 0
sum_b = 0
for i in S:
    if(i == 'a'):
        if((sum_a + sum_b) < (A+B)):
            print('Yes')
            sum_a +=1
        else:
            print('No')
    elif(i == 'b'):
        if((sum_a + sum_b) < (A+B) and sum_b < B):
            print('Yes')
            sum_b +=1
        else:
            print('No')
    else:
        print('No')