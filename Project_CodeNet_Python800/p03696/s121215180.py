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
	
	A=[]
	if s[0]==")":
		A.append(0)
	s+="0"
	cnt=1
	for i in range(n):
		if s[i]==s[i+1]:
			cnt+=1
		else:
			A.append(cnt)
			cnt=1
	#print(A)
	
	l=0
	r=0
	now=0
	for i in range(len(A)):
		#print(r)
		if i%2:
			r+=2*min(A[i],now)
			l+=max(A[i]-now,0)
			now=max(now-A[i],0)
		else:
			now+=A[i]
	#print(l,n-l-r)
	
	ans="("*l+s[:-1]+")"*(n-l-r)
	print(ans)
	
	
	
	
	
	

if __name__=="__main__":
	main()
