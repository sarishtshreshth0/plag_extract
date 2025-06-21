import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    
x,y=map(int,input().split())

print(x+y//2)