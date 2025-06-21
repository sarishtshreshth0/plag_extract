import sys
input = sys.stdin.readline

A,B = list(map(int,input().split()))
A = (A-2)%13
B = (B-2)%13
print('Alice' if A>B else 'Bob' if B>A else 'Draw')
