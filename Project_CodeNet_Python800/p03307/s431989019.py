import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')

N=int(input())

if N%2==0:
	N=N//2

print(N*2)