

#import sys
#import os
#import re
#import datetime

N = int(input())
#print(input().split())
a = list(map(int, input().split()))
#print(a)
countA = {}
for v in a:
	for i in (-1,0,1):
		#print("i = {}".format(i))
		if(v - i in countA):
			countA[v - i] = countA[v - i] + 1
		else:
			countA[v - i] = 1
print(max(countA.values()))

#town = {}
#for _ in range(N):
#	S, P = input().split()
#	town[S] = int(P)
#
#sum2 = sum(town.values()) / 2
#for S, P in town.items():
#	if P > sum2:
#		print(S)
#		break
#else:
#	print('atcoder')