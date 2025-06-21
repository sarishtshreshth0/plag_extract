# -*- coding: utf-8 -*-
def main():
    N, A, B = map(int, input().split())
    S = input()
    kakutei = 0
    kaigai_rank = 1
    check = False
    for s in S:
        if kakutei < A+B:
            if s == 'a':
                kakutei += 1
                print('Yes')
            elif s == 'b':
                if kaigai_rank <= B:
                    kaigai_rank += 1
                    kakutei += 1
                    print('Yes')
                else:
                    check = True
                    print('No')
            elif s == 'c':
                print('No')
            # print('kakutei: ' + str(kakutei))
            # print('rank: ' + str(kaigai_rank))
        else:
            print('No')
            
if __name__ == '__main__':
    main()

# No
# Yes
# Yes
# Yes
# Yes
# No
# Yes
# Yes
# No
# Yes
# No
# No
