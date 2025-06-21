#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))
  
n=int(input())
W=input_array()

left=0
right=sum(W)
diff=right

for i in range(n):
	left+=W[i]
	right-=W[i]
	diff_tmp=right-left
	# print(diff,diff_tmp)
	if abs(diff)<=abs(diff_tmp):
		print(abs(diff))
		break
	else:
		diff=diff_tmp