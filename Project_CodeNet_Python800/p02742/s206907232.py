h,w = map(int, raw_input().split(' '))
def f(h,w):
	if h == 1 or w == 1:
		return 1
	x = w - w/2
	y = w/2
	count = 0
	count += (h - (h/2)) * x
	count += ((h/2)) * y
	return count
		


print f(h,w)