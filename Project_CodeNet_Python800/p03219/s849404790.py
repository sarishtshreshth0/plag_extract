import sys

#+++++
		
def main():
	b , c = map(int, input().split())
	ret=b+(c//2)
	print(ret)
	
	
#+++++

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)