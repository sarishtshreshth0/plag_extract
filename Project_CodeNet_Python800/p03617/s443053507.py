from sys import stdin

q,h,s,d = [int(x) for x in stdin.readline().split()]
n = int(stdin.readline().strip())

min_for_one = min([q*4, h*2, s])
min_for_two = min([min_for_one*2, d])

print(n//2*min_for_two + n%2*min_for_one)