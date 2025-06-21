import collections

def gcd(u,v):
	if v:
		return gcd(v, u % v)
	else:
		return u

n = int(raw_input())
elems = map(int , raw_input().split(' '))
dpp = [ None ] * len(elems)
dps = [ None ] * len(elems)
dpp[0] = elems[0]
for i in range(1,len(elems)): 
	dpp[i] = gcd(elems[i], dpp[i-1])
dps[len(elems) -1]  = elems[-1]
for i in range(len(elems) - 2, -1, -1): 
	dps[i] = gcd(elems[i], dps[i+1])
r = 0
for i in range(len(elems)):
	u,v = dpp[i-1] if i-1 >= 0 else -1, dps[i+1] if i+1 < len(elems) else -1
	r  = max(r, gcd(u,v) if u != -1 and v != -1 else max(u,v))
print r

