def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

if __name__ == '__main__':
	
	n = int(input())

	#n = a * b のためnの約数を求める
	A = divisor(n)

	B = []
	c_tmp = 11
	
	for i in A:
		tmp = n // i
		#tmp i の桁数をチェック
		c1 = len(str(tmp))
		c2 = len(str(i))
		c2_tmp = max(c1,c2)
		c_tmp = min(c2_tmp,c_tmp)

	print(c_tmp)


