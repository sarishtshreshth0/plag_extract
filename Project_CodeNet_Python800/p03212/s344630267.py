import sys
import collections

#+++++

def count_max(a_len, using):
	if a_len < 3:
		return 0
	
	total = 3 ** a_len
	
	#33...33, 55...55,77...77
	all_single = 3 - len(using)
	
	#333553535
	tt = 2 ** a_len - 2
	
	



def main():
	n = int(input())
	#b , c = map(int, input().split())
	#s = input()
	ret = 0
	q = collections.deque()
	if n < 357:
		return 0
	
	for i, v in enumerate([3,5,7]):
		q.append((v, 1, 2**i))
		
	while q:
		value, keta, is_full = q.popleft()
		#print(value,keta,is_full)
		for i, v in enumerate([3,5,7]):
			n_value = value + v*(10**keta)
			if n_value > n:
				continue
			n_is_full = is_full | (2**i)
			if n_is_full == 7:
				ret += 1
			q.append((n_value, keta+1, n_is_full))
	
	print(ret)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)