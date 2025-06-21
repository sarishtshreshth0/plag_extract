# from geek for geeks
# a^(a+1)^(a+2).....^(a+k) = (a^(a+1))^((a+2)^(a+3))^((a+4)^(a+5)).....((a+k-1)^(a+k))
# we can pair every two adjacent no and their xor will be 1 because of lsb
def main():
	a , b = map(int , input().split())
	a=a-1
	rem = a%4
	x, y =0 ,0
	if rem==0:# this mean no of 1's is even (1 is result of xor of each pair)
		x=a   # and we are left with only a no pair for this element
	elif rem==1:# this means every no is successfully paired and no of ones is odd
		x=1
	elif rem==2: # this means last element is not paired and no of one's is odd and 
		x = a+1		# a is even no so ans 1^a
	else:
		x=0		# every no is succesfully paired and no of 1 is even so xor is 0	
	rem = b%4
	if rem ==0:
		y=b
	elif rem==1:
		y=1
	elif rem==2:
		y=b+1
	else:
		y=0
	print(x^y)
if __name__=="__main__":
	main()