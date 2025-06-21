def f(x):
	q = 0
	c = x
	while(x):
	  q += x % 10
	  x /=10
	return c and c % q == 0
print 'Yes' if f(int(raw_input())) else 'No'