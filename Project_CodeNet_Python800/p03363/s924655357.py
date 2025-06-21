import sys
input = sys.stdin.readline

import collections
import random

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def dist(x1,y1,x2,y2):
	return abs(x1-x2)+abs(y1-y2)

def testInput():
	n = 2* 10**5
	def ran():
		#return random.randint(-10**9,10**9)
		return 0
	va = [ran() for _ in [0,]*n]
	return n, va

def main():
	N = int(input())
	vA = linput()
	
	#N,vA=testInput()
	#print(N,vA[:5])
	
	vC = [0,]
	s = 0
	for a in vA:
		s += a
		vC.append(s)
	
	cC = collections.Counter(vC)
	#print(cC)
	
	res = 0
	for p,c in cC.items():
		#print(p,c)
		res += c*(c-1)//2
	
	print(res)
	#sT = "No Yes".split()
	#print(sT[res])
	

if __name__ == "__main__":
	main()
