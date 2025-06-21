n, a, b = map(int, input().split())  
sList = input()
cnt = 0
cnt_b = 0
for i, s in enumerate(sList):
    if s == 'a':
        #国内の学生は、現在予選の通過が確定した参加者がA+B人に満たなければ、予選を通過する
        if cnt < a+b:
            cnt += 1
            print('Yes')
        else:
            print('No')
    elif s == 'b':
        #さらに海外の学生の中での順位がB位以内なら、予選を通過する
        if (cnt < a+b) & (cnt_b < b):
            cnt += 1
            cnt_b += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')