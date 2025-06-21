import numpy
s = numpy.array(list(input()))
t = numpy.array(list(input()))
ns = len(s)
nt = len(t)
match = s.reshape(-1,1) == t.reshape(1,-1)
memo = numpy.zeros([ns+1, nt+1], dtype = int)
for i in range(ns):
    memo[i+1, 1:] = numpy.fmax(memo[i, :-1]+match[i], memo[i, 1:])
    
    memo[i+1] = numpy.maximum.accumulate(memo[i+1])
ans = []
while ns >0 and nt>0:
    if memo[ns, nt] == memo[ns-1, nt]:
        ns -= 1
    elif memo[ns, nt] == memo[ns, nt-1]:
        nt -= 1
    else:
        ans.append(s[ns-1])
        
        nt-=1
        ns -=1
print("".join(ans[::-1]))