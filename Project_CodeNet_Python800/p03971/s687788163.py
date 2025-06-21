n, a, b = map(int, input().split())
s = input()
sum_ = 0
b_cnt = 0
for i in range(n):
    #print(sum_, b_cnt)
    if s[i] != 'c' and sum_ < a + b:
        if s[i] == 'a':
            print('Yes')
            sum_ += 1
            continue
        elif s[i] == 'b' and b_cnt < b:
            print('Yes')
            b_cnt += 1
            sum_ += 1
            continue
    
    print('No')