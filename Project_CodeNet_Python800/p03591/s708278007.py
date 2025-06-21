import sys
S = input()

if len(S)<4:
    print('No')
    sys.exit()


if S[0] == 'Y':
    if S[1] == 'A':
        if S[2] == 'K':
            if S[3] == 'I':
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
