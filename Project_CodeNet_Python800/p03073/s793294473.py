s = input()
l= len(s)
 
if l== 1:
    print(0)
    exit()
 
even = s[::2]
odd = s[1::2]

odd_zero = odd.count("0")
even_one = even.count("1")
 

odd_one = odd.count("1")
even_zero = even.count("0")
 
print(min(odd_zero + even_one, odd_one + even_zero))