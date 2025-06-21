import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

bn = 2 ** 42

def bb(v):
	ra = bin(v+bn)[3:][::-1]
	return ra

def cc(v, i):
	r = pow(2, i)
	vn = v+1
	vna = vn //(2*r)
	vnb = vn % (2*r)
	ret = vna * r
	ret += max(vnb - r, 0)
	#pa((v,i,ret))
	return ret

def main():
	#a = int(input())
	f, t = tin()
	#s = input()
	ret = 0
	for i, _ in enumerate(bb(0)):
		r = pow(2, i)
		nn = cc(t,i) - cc(f-1, i)
		if (nn) % 2 == 1:
			#pa(r)
			ret += r
	return ret
		
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)