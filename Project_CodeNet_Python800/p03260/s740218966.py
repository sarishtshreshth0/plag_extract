import sys
A,B = map(int,input().split())
if not (1 <= A <= 3 and 1 <= B <= 3):
    sys.exit()

print('Yes') if ( A * B ) % 2 == 1 else print('No')