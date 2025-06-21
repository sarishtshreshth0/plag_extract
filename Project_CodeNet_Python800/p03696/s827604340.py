import sys


#input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()


def II(): return int(input())


def MI(): return map(int,input().split())


def MF(): return map(float,input().split())


def LI(): return list(map(int,input().split()))


def LF(): return list(map(float,input().split()))


def TI(): return tuple(map(int,input().split()))


# rstrip().decode('utf-8')


def main():
	n=II()
	s=input()
	ss=s
	for _ in range(100):
		s=s.replace("()","")
	ans="("*s.count(")")+ss+")"*s.count("(")
	print(ans)
	
	
	





	

if __name__=="__main__":
	main()
