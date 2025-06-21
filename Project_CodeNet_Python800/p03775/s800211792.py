import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

def main():
	ans=15
	n=II()

	nn=int(n**0.5)+10

	for i in range(1,nn):
		if n%i==0:
			a=len(str(i))
			b=len(str(n//i))
			ans=min(ans,max(a,b))
			#print(a,b)

	print(ans)




if __name__ == "__main__":
	main()
