import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    
a,b,c=map(int,input().split())

if (a-c)*(b-c)<0:
	print("Yes")
else:
	print("No") 