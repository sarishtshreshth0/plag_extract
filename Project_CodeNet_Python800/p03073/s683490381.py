s = input()
s1 = s[0::2]
s2 = s[1::2]

t1 = s1.count('1') + s2.count('0')
t2 = s1.count('0') + s2.count('1')
print(min(t1, t2))